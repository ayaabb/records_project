import os


def get_record_dict():
    file_name = os.environ.get("file_name")
    records = get_record_dict(file_name)