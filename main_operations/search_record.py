from log.log_to_file import *
from helper_functions.print_records import print_records_with_details
from file_handle.convert_txtFile_to_dictionary import get_record_dict


def search_record(record_name):
    records = get_record_dict()
    list_record_names = search_record_by_substring(record_name, records)

    if len(list_record_names) == 0:
        print(f"Record search failed: No results found for the {record_name}")
        log_messages_to_file('Search', 'Failed')
    else:
        log_messages_to_file('Search', 'Succeed')
        print("Search results:")
        print_records_with_details(records, sorted(list_record_names), copies=True)


def search_record_by_substring(record_name, records):
    record_result = []
    for record in records.keys():
        if record_name in record:
            record_result.append(record)

    return record_result
