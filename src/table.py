from jinja2 import Template
from pathlib import Path, PosixPath
import json
import csv
from copy import deepcopy
from google.cloud import bigquery

import google.api_core.exceptions

from src.base import Base
from src.storage import Storage
from src.dataset import Dataset


class Table(Base):
    def __init__(self, table_id, dataset_id, **kwargs):
        super().__init__(**kwargs)

        self.table_id = table_id.replace("-", "_")
        self.dataset_id = dataset_id.replace("-", "_")
        self.dataset_folder = Path(self.metadata_path / self.dataset_id)
        self.table_folder = self.dataset_folder / table_id
        self.table_full_name = dict(
            prod=f"{self.client['bigquery_prod'].project}.{self.dataset_id}.{self.table_id}",
            staging=f"{self.client['bigquery_staging'].project}.{self.dataset_id}_staging.{self.table_id}",
        )
        self.table_full_name.update(dict(all=deepcopy(self.table_full_name)))

    @property
    def table_config(self):
        return self._load_yaml(self.table_folder / "table_config.yaml")

    def _get_table_obj(self, mode):
        return self.client[f"bigquery_{mode}"].get_table(self.table_full_name[mode])

    def _load_schema(self, mode="staging", with_partition=True):
        """Load schema from table_config.yaml"""

        self._check_mode(mode)

        json_path = self.table_folder / f"schema-{mode}.json"

        columns = self.table_config["columns"]

        if mode == "staging":
            for c in columns:
                c["type"] = "STRING"

            columns = [c for c in columns if c["is_in_staging"]]

            if not with_partition:
                columns = [c for c in columns if not c.get("is_partition")]

        elif mode == "prod":
            schema = self._get_table_obj(mode).schema

            for c in columns:
                for s in schema:
                    if c["name"] == s.name:
                        c["type"] = s.field_type
                        c["mode"] = s.mode

        json.dump(columns, (json_path).open("w"))

        return self.client[f"bigquery_{mode}"].schema_from_json(str(json_path))

    def init(self, data_sample_path=None, if_exists="raise"):
        """Initialize table folder at metadata_path at
        `metadata_path/<dataset_id>/<table_id>`.

        The folder should contain:
            - table_config.yaml
            - publish.sql

        You can also point to a sample of the data to auto complete columns names.

        Parameters
        ----------
        data_sample_path : (str, pathlib.PosixPath), optional
            Data sample path to auto complete columns names, by default None.
            It supports Comma Delimited CSV.
        if_exists : str, optional
            What to do if table folder exists, by default "raise"
            - 'raise' : Raises FileExistsError
            - 'replace' : Replace folder
            - 'pass' : Do nothing

        Raises
        ------
        FileExistsError
            If folder exists and replace is False.
        NotImplementedError
            If data sample is not in supported type or format.
        """

        if not self.dataset_folder.exists():

            raise FileExistsError(
                f"Dataset folder {self.dataset_folder} folder does not exists. "
                "Create a dataset before adding tables."
            )

        try:
            self.table_folder.mkdir(exist_ok=(if_exists == "replace"))
        except FileExistsError:
            if if_exists == "raise":
                raise FileExistsError(
                    f"Table folder already exists for {self.table_id}. "
                )
            elif if_exists == "pass":
                return self

        if isinstance(
            data_sample_path,
            (
                str,
                PosixPath,
            ),
        ):
            data_sample_path = Path(data_sample_path)
            if data_sample_path.suffix == ".csv":

                columns = next(csv.reader(open(data_sample_path, "r")))

            else:
                raise NotImplementedError(
                    "Data sample just supports comma separated csv files"
                )
        else:
            columns = ["column_name"]

        for file in (Path(self.templates) / "table").glob("*"):

            if file.name in ["table_config.yaml", "publish.sql"]:

                # Load and fill template
                template = Template(file.open("r").read()).render(
                    table_id=self.table_id,
                    dataset_id=self.dataset_folder.stem,
                    project_id=self.client["bigquery_staging"].project,
                    columns=columns,
                )

                # Write file
                (self.table_folder / file.name).open("w").write(template)

        return self

    def create(
        self,
        filepath=None,
        job_config_params=None,
        partitioned=False,
        if_exists="raise",
        force_dataset=True,
    ):
        """Creates BigQuery table at staging dataset.

        If you add a filepath, it automatically saves the data in the storage,
        creates a datasets folder and BigQuery location, besides creating the
        table and its configuration files.

        The new table should be located at `<dataset_id>_staging.<table_id>` in BigQuery.

        It looks for data saved in Storage at `<bucket_name>/staging/<dataset_id>/<table_id>/*`
        and builds the table.

        It currently supports the types:
            - Comma Delimited CSV

        Data can also be partitioned following the hive partitioning scheme
        `<key1>=<value1>/<key2>=<value2>`, for instance, `year=2012/country=BR`

        TODO: Implement if_exists=raise
        TODO: Implement if_exists=pass

        Parameters
        ----------
        filepath : str or pathlib.PosixPath
            Where to find the file that you want to upload to create a table with
        job_config_params : dict, optional
            Job configuration params from bigquery, by default None
        partitioned : bool, optional
            Whether data is partitioned, by default False
        if_exists : str, optional
            What to do if table exists, by default "raise"
            - 'raise' : Raises Conflict exception
            - 'replace' : Replace table
            - 'pass' : Do nothing
        force_dataset: bool, by default True
            Creates <dataset_id> folder and BigQuery Dataset if it doesn't
            exists.
        """

        # Add data to storage
        if isinstance(
            filepath,
            (
                str,
                PosixPath,
            ),
        ):

            Storage(self.dataset_id, self.table_id, **self.main_vars).upload(
                filepath, mode="staging", if_exists="replace"
            )

            # Create Dataset if it doesn't exist
            if force_dataset:

                dataset_obj = Dataset(self.dataset_id, **self.main_vars)

                try:
                    dataset_obj.init()
                except FileExistsError:
                    pass
                    
                dataset_obj.create(if_exists="pass")

            self.init(data_sample_path=filepath, if_exists="replace")

        if job_config_params is None:

            job_config_params = dict(
                write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
                source_format=bigquery.SourceFormat.CSV,
                skip_leading_rows=1,
            )

        if isinstance(job_config_params, dict):

            job_config_params.update(
                dict(
                    schema=self._load_schema("staging", with_partition=False),
                    destination_table_description=self._render_template(
                        "table/table_description.txt", self.table_config
                    ),
                )
            )

        if partitioned:

            hive_partitioning = bigquery.external_config.HivePartitioningOptions()
            hive_partitioning.mode = "AUTO"
            hive_partitioning.source_uri_prefix = self.uri.format(
                dataset=self.dataset_id, table=self.table_id
            ).replace("*", "")

            job_config_params["hive_partitioning"] = hive_partitioning

        job_config = bigquery.LoadJobConfig(**job_config_params)

        if if_exists == "replace":
            self.delete(mode="staging")

        load_job = self.client["bigquery_staging"].load_table_from_uri(
            self.uri.format(
                dataset=self.table_config["dataset_id"],
                table=self.table_config["table_id"],
            ),
            self.table_full_name["staging"],
            job_config=job_config,
        )

        load_job.result()

        self.update(mode="staging")

    def update(self, mode="all", not_found_ok=True):
        """Updates BigQuery schema and description.

        Parameters
        ----------
        mode : str, optional
            Table of which table to update [prod|staging|all], by default "all"
        not_found_ok : bool, optional
            What to do if table is not found, by default True
        """

        self._check_mode(mode)

        if mode == "all":
            mode = ["prod", "staging"]
        else:
            mode = [mode]

        for m in mode:

            try:
                table = self._get_table_obj(m)
            except google.api_core.exceptions.NotFound:
                continue

            table.description = self._render_template(
                "table/table_description.txt", self.table_config
            )
            table.schema = self._load_schema(m)

            self.client[f"bigquery_{m}"].update_table(
                table, fields=["description", "schema"]
            )

    def publish(self, if_exists="raise"):
        """Creates BigQuery table at production dataset.

        Table should be located at `<dataset_id>.<table_id>`.

        It creates a view that uses the query from
        `<metadata_path>/<dataset_id>/<table_id>/publish.sql`.

        Make sure that all columns from the query also exists at
        `<metadata_path>/<dataset_id>/<table_id>/table_config.sql`, including
        the partitions.

        Parameters
        ----------
        if_exists : str, optional
            What to do if table exists, by default "raise"
            - 'raise' : Raises Conflict exception
            - 'replace' : Replace table
            - 'pass' : Do nothing
        """

        # TODO: check if all required fields are filled

        view = bigquery.Table(self.table_full_name["prod"])

        view.view_query = (self.table_folder / "publish.sql").open("r").read()

        view.description = self._render_template(
            "table/table_description.txt", self.table_config
        )

        if if_exists == "replace":
            self.delete(mode="prod")

        self.client["bigquery_prod"].create_table(view)

        self.update("prod")

    def delete(self, mode):
        """Deletes table.

        Parameters
        ----------
        mode : str
            Table of which table to delete [prod|staging|all]
        """

        self._check_mode(mode)

        if mode == "all":
            for m, n in self.table_full_name[mode].items():
                self.client[f"bigquery_{m}"].delete_table(n, not_found_ok=True)
        else:
            self.client[f"bigquery_{mode}"].delete_table(
                self.table_full_name[mode], not_found_ok=True
            )

    def append(self, filepath, partitions=None, if_exists="raise", **upload_args):

        Storage(self.dataset_id, self.table_id, **self.main_vars).upload(
            filepath, mode="staging", partitions=None, if_exists="raise", **upload_args
        )

        self.create(if_exists="replace")
