from . import config
import requests

def query(sobject:str, fields:list):
    url = f"{config.instance_url}{config.data_path_url}{config.query_endpoint}"
    print(url)
    fields.remove("Id")
    params = {
        "q": f"SELECT Id, {", ".join(fields)} FROM {sobject}"
    }
    r = requests.get(url=url, params=params, headers=config.configuration.header)
    return r.json()

def queryLocator():
    url = f"{config.instance_url}{config.data_path_url}{config.query_endpoint}"
    print(url)
    r = requests.get(url=url, headers=config.configuration.header)
    return r.json()