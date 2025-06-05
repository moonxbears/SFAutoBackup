import requests
import json

instance_url = "https://asphaltzipper.my.salesforce.com"
auth_path = "/services/oauth2/token"
data_path_url = "/services/data/v63.0"
query_endpoint = "/query"
query_locate_endpoint = "/query/queryLocator"
sobject_endpoint = "/sobjects"

configuration = type('', (), {
    "access_token": "", 
    "id": "", 
    "token_type": "", 
    "issue_dtime": "", 
    "signature": "", 
    "api_url": "", 
    "scope": "", 
    "token_format": "",
    "header": {},
})()

with open("secret", "r") as file:
    client_key = file.readline() # first line in secret file contains salesforce rest api client key
    client_secret = file.readline() # second line in secret file contains salesforce rest api client secret

auth_data = {
    "grant_type": "client_credentials",
    "client_id": client_key,
    "client_secret": client_secret,
}

def authorize():
    url = f"{instance_url}{auth_path}"
    r = requests.post(url=url, data=auth_data)
    if r.status_code == 200:
        rjson = r.json()
        configuration.access_token    = rjson["access_token"]
        configuration.id              = rjson["id"]
        configuration.token_type      = rjson["token_type"]
        configuration.issue_dtime     = rjson["issued_at"]
        configuration.signature       = rjson["signature"]
        configuration.api_url         = rjson["api_instance_url"]
        configuration.scope           = rjson["scope"]
        configuration.token_format    = rjson["token_format"]
        configuration.header = {
            "Authorization": f"{configuration.token_type} {configuration.access_token}"
        }
        return True
    return False