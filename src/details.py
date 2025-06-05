from . import config
import requests
import json

def get_objects():
    url = f"{config.instance_url}{config.data_path_url}{config.sobject_endpoint}/"
    print(url)
    r = requests.get(url=url, headers=config.configuration.header)
    return r.json()["sobjects"]

def get_fields(SFObject:str):
    url = f"{config.instance_url}{config.data_path_url}{config.sobject_endpoint}/{SFObject}/describe/"
    print(url)
    r = requests.get(url=url, headers=config.configuration.header)
    return r.json()["fields"]
