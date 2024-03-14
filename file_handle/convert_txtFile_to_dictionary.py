import os


def get_record_dict():
    file_name = os.environ.get("file_name")
    file = open(str(file_name),'r')
    lines = file.readlines()
    records = {}
    for line in lines:
        details = line.split(', ')
        records[details[0]] = int(details[1])
    return records
    
    # records = get_record_dict(file_name)
