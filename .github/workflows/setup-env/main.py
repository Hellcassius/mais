import os
import shutil
from pathlib import Path
import base64
import json
import toml
import tomlkit


def decoding_base64(message):
    # decoding the base64 string
    base64_bytes = message.encode("ascii")
    message_bytes = base64.b64decode(base64_bytes)
    return message_bytes.decode("ascii")


def create_config_folder(config_folder):
    ## if ~/.basedosdados folder exists delete
    if os.path.exists(Path.home() / config_folder):
        shutil.rmtree(Path.home() / config_folder, ignore_errors=True)
    ## create ~/.basedosdados folder
    os.mkdir(Path.home() / config_folder)
    os.mkdir(Path.home() / config_folder / "credentials")


def save_json(json_obj, file_path, file_name):
    ### function to save json file
    with open(Path(file_path) / file_name, "w", encoding="utf-8") as f:
        json.dump(json_obj, f, ensure_ascii=False, indent=2)


def create_json_file(message_base64, file_name, config_folder):
    ### decode base64 script and load as a json object
    json_obj = json.loads(decogind_base64(message_base64))
    prod_file_path = Path.home() / config_folder / "credentials"
    ### save the json credential in the .basedosdados/credentials/
    save_json(json_obj, prod_file_path, file_name)


def save_toml(config_dict, file_name, config_folder):
    ### save the config.toml in .basedosdados
    file_path = Path.home() / config_folder
    with open(file_path / file_name, "w") as toml_file:
        toml.dump(config_dict, toml_file)


def create_config_tree(prod_base64, staging_base64, config_dict):
    ### execute the creation of .basedosdados
    create_config_folder(".basedosdados")
    ### create the prod.json secret
    create_json_file(prod_base64, "prod.json", ".basedosdados")
    ### create the staging.json secret
    create_json_file(staging_base64, "staging.json", ".basedosdados")
    ### create the config.toml
    save_toml(config_dict, "config.toml", ".basedosdados")


def main():
    # print(json.load(Path("/github/workspace/files.json").open("r")))
    # print(os.environ.get("INPUT_PROJECT_ID"))
    print(Path.home())

    workspace = Path(".")

    print(
        "########################  WORKSPACE   #########################################"
    )
    print(workspace)

    ### json with information of .basedosdados/config.toml
    config_dict = {
        "metadata_path": str(Path("/github") / "workspace" / "bases"),
        "templates_path": str(
            Path("/github") / "workspace" / "basedosdados" / "configs" / "templates"
        ),
        "bucket_name": "test13-01-bucket",
        "gcloud-projects": {
            "staging": {
                "name": "test13-01",
                "credentials_path": str(
                    Path.home() / ".basedosdados" / "credentials" / "staging.json"
                ),
            },
            "prod": {
                "name": "test13-01",
                "credentials_path": str(
                    Path.home() / ".basedosdados" / "credentials" / "prod.json"
                ),
            },
        },
    }
    print(
        "################################################################################################"
    )
    print(config_dict)
    print(
        "################################################################################################"
    )
    ### load the secret of prod and staging data
    prod_base64 = os.environ.get("INPUT_PROD")
    staging_base64 = os.environ.get("INPUT_STAGING")

    ### create config and credential folders
    create_config_tree(prod_base64, staging_base64, config_dict)


if __name__ == "__main__":
    main()