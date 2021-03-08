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
    json_obj = json.loads(decoding_base64(message_base64))
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

    workspace = Path(".").resolve()

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
    prod_base64 = """"ewogICJ0eXBlIjogInNlcnZpY2VfYWNjb3VudCIsCiAgInByb2plY3RfaWQiOiAidGVzdDEzLTAx
    IiwKICAicHJpdmF0ZV9rZXlfaWQiOiAiNTMxZjY5ZTg4ZTA1NDcxYjJhMWU4ZWVmMmU2NzVkNjE3
    MTNlZWMzYiIsCiAgInByaXZhdGVfa2V5IjogIi0tLS0tQkVHSU4gUFJJVkFURSBLRVktLS0tLVxu
    TUlJRXZnSUJBREFOQmdrcWhraUc5dzBCQVFFRkFBU0NCS2d3Z2dTa0FnRUFBb0lCQVFDcXJaSlJh
    aEpmcVgzSFxuWWdxdXlLU25iVVNzTW5acWRiY0k0VlgxeGQ0eWZEV29iL0FIOGxnYjc2b2x5WG1u
    SEkrdXQ3K0hMN0Vzb2d2clxuQTJWenNPbjRrRWRXcU5ZTGV0Rys4aWNmVllOSXQyeERFV0hPZWg2
    TGJiRWpuWjZxaGM5aU1HWlJGL3pzSEZOelxudnhTU2doVkxESFQ2UGZHVDFNaWVIdDUyVTlxT3Fa
    RTEwSkFHRGhFcmFoWnUxLzF5ekxvaVMvQXJGYWRHdjFQeVxuQitWTy9BU1VCMUl1VEFhVXhtZURs
    K1cwa1ZxLzBmLzBYM1I0SVBURkpWWE14eGQ0RjBJL1J1dWhZRjh6ZlhpRFxucHJDaG82Vno0THE0
    NjBDVzhDV0JPYzNEWnc5R09wZmJJM25HTGUvYnNTSUNVWmtEMlRJUXpQL1R2NHJLTWIyZVxuZVdN
    QS94YW5BZ01CQUFFQ2dnRUFUWjBFam5VM3lieWZiODJMb2hPbm5HTTUrVHd4VVJRYW1iVXVpOGJn
    MWdCWlxudmpDNDdFUXVBUFlwWDJtUklvY0FaNmt6TlZ4Z3F6VTlTaStQTU43Z1pxSGxidWp6L09C
    ckJQUEZDcUN1UktEMFxuWUVORlFNbVRuai9SYjZxN2ZqdS9KSjF4eWFxbzN3MjZmVVlGS3VKd29H
    SVh4N3ZuWVJ3LzVuZVBIaXZmbFVPVVxuaTRKaWJnbHVIT1hlbG1hUXVpemEvUEwxOVM0RTAxQXRF
    MGVuUi9TQUxWMmlXZWF3YmIwbEZYT1dKeDBZU09xNFxuRnZ1RVJKVklKSHBCclByUnhQSzlMRmR1
    Tzkxam1qYUs3amNnNitpOWh2U1Z5b2M5NUtnUzIxSUsxOFdhblQzTFxuc05hZmhraExsdzN5dDYw
    UDR3d2tEeWN3bG4rWFM2U0Y2eGxlMXlOQmdRS0JnUURYbXQ5ZjBDU1ZoTkdvTWFRb1xuNnhMbW9E
    bFBaM2pwdWNXbnpOd0tmTm9NWlRreW96T01aVTBVRVdrdkFhUkFPeTVNNFg5YlB0L0xtdlJnMTRK
    ZlxuYVZuQ1ZQMUhWci96aU1aeVZuV1pVOVlNRUxQek5JYmltS2RqNzBYc1lDdzBYcVVCMXZFclM3
    c2pIZ0lTekxKQVxueTRWb0UyWFhFMnY0b1VENjl0amtzbTdaUndLQmdRREtwOXFDM0RkWGUrTE91
    RTRKaXAyZnJYUHRreTZRajlYelxucHp3NCtJeVdkcjFib0VDa05FVlZBUmo3K3VaZnlicWdVTkFY
    MlRBQ1JXOTA0eWdKL2NNUW9YVExDZURWU3hLRFxuNlN6b0VTa1NGSFIzSDBMcCtpMnZQb1RDSitk
    QTdnR1NZczNybmRMZktkN2ZtMVNMNFNmTWIzd255cmdHUlBJTlxuZWloTlg2eUhvUUtCZ1FDazRl
    eW5zbDczOVczOHFaSDROT1hzZDJXOG9zM21PRXEvSzd5dlRKSFlYdVRpSThyOVxuT0U4ODVKL0M4
    Z2R4azVDeC9OVlBxNEtzaTZFT0dtRzZvNitnSFN6aERLZVpEK1ZyZFZGVDQ3aFMyOGN5Vzk0M1xu
    bGpTVkNWdzVDOGRpZVdySlFGNkpGTTVWYWRKK0hBcko0SnJ5WDd0SFFyUVVuUVU3cCtGdzdFQTNh
    d0tCZ0U2QVxucFRHcDhyb3Q0RmNwcC9ra1BCajl6UG1MMlM3Z3VRVndrL0NSdjR3TnBSNllQbElk
    ZVhvTE9jMXFqTkV3U040UFxuVC96ZEFpN3ZETlRmcGNQeERCNG1IU01GeVpWMlJrN1pCYTlEN24v
    MWNvUXVsUElrR294WEVJQlJpdEJwSWl5OVxubjMwVkh2bVpzNTgxQVpSSi9PdkJoL3UyR0lFOU5m
    S29qbklpaktmaEFvR0JBTUI0UHJmSFJFYjRhTlF6NjF0b1xub2l5d0JGZzVIakNCcUZjU0M5WlZo
    QjBVN2pJU1ljWXEwa0VqY0FIN0ptcHhXQWIzcDRDV0ZObWVDcCswTzZSTFxuR21KNElYNUR1TnJx
    eVNYYVJ2MTIwYWM2UzQ2elFUY3lRVC8zR05Ld3FoeGYyOFpmV2RraDJVK2xyYVV6Y2oyZ1xuQjJ5
    ZW1uN092U1FBTzVVcVgrREZyNURaXG4tLS0tLUVORCBQUklWQVRFIEtFWS0tLS0tXG4iLAogICJj
    bGllbnRfZW1haWwiOiAiY2Fpby04MTdAdGVzdDEzLTAxLmlhbS5nc2VydmljZWFjY291bnQuY29t
    IiwKICAiY2xpZW50X2lkIjogIjEwMTIzMTk3ODk0OTEzNDk2ODExOSIsCiAgImF1dGhfdXJpIjog
    Imh0dHBzOi8vYWNjb3VudHMuZ29vZ2xlLmNvbS9vL29hdXRoMi9hdXRoIiwKICAidG9rZW5fdXJp
    IjogImh0dHBzOi8vb2F1dGgyLmdvb2dsZWFwaXMuY29tL3Rva2VuIiwKICAiYXV0aF9wcm92aWRl
    cl94NTA5X2NlcnRfdXJsIjogImh0dHBzOi8vd3d3Lmdvb2dsZWFwaXMuY29tL29hdXRoMi92MS9j
    ZXJ0cyIsCiAgImNsaWVudF94NTA5X2NlcnRfdXJsIjogImh0dHBzOi8vd3d3Lmdvb2dsZWFwaXMu
    Y29tL3JvYm90L3YxL21ldGFkYXRhL3g1MDkvY2Fpby04MTclNDB0ZXN0MTMtMDEuaWFtLmdzZXJ2
    aWNlYWNjb3VudC5jb20iCn0K"""
    staging_base64 = prod_base64

    ### create config and credential folders
    create_config_tree(prod_base64, staging_base64, config_dict)


if __name__ == "__main__":
    main()