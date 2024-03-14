from log.log_to_file import log_messages_to_file
from file_handle.convert_txtFile_to_dictionary import *
from helper_functions.print_records import print_records_with_details


def print_all_records():
    records = get_record_dict()
    list_record_names = records.keys()
    sorted_names = sorted(list_record_names)
    if len(list_record_names) == 0:
        print("No records founded!")
        return
    for record in sorted_names:
        log_messages_to_file("Print All",record, str(records[record]))
    print_records_with_details(records, sorted_names, copies=True)
