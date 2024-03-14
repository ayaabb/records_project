from log.log_to_file import log_messages_to_file
from file_handle.update_file import *
from file_handle.convert_txtFile_to_dictionary import get_record_dict
from main_operations.delete_record import *


def insert_record(record_name, copies):
    try:
        records = get_record_dict()
        record_name, old_copies, Inserted = remove_record_to_overwrite(records, record_name,
                                                                       'add', copies, new_record=True)
        if not Inserted:
            raise Exception

        write_to_file(record_name + ", " + str(copies + old_copies))
        log_messages_to_file("Insert", "Success")
        print(f"'{record_name}' record insertion succeed\n")
    except Exception:
        log_messages_to_file("Insert", "Failure")
        print(f"'{record_name}' record insertion failed\n")

