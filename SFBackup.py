import argparse as arg
from logging import debug
from src import details, config, query
import json


sfobjects:list

def get_backup_fields(fields:list):
    # fields_list = []
    # print(fields)
    # for f in fields:
    #     if f["permissionable"] == True:
    #         name = f["name"]
    #         fields_list.append(name)
    #         print(name)
    return [f["name"] for f in fields]#if f["permissionable"] == True]

def sf_object_backup(sobject):
    collection = [o for o in sfobjects if o["name"] == sobject and o["queryable"] == True]
    if len(collection) > 0:
        sobject_details = collection[0]
        field_list = get_backup_fields(details.get_fields(sobject))
        
        return field_list
    else:
        debug(f"unable to find {sobject} salesforce object with that api name and is queryable")

def main():
    parser = arg.ArgumentParser()
    parser.add_argument("--objects", required=True, type=str, nargs='+', help="the salesforce object api names' to backup with all of their fields")
    parser.add_argument("-o", "--output-path", type=str, required=True, help="designate the output for the backups. Structure is path > backup [Date] > [object].csv (one or multiple)")
    parser.add_argument("-v", "--verbose", action="store_true")

    args = parser.parse_args()
    
    if not config.authorize():
        return
    
    global sfobjects
    sfobjects = details.get_objects()
    
    for sobject in args.objects:
        fields = sf_object_backup(sobject)
        qresults = query.query(sobject, fields)
        print(query.queryLocator())

if __name__ == "__main__":
    main()