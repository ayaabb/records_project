from ask_user import ask_for_option_record
from log_to_file import log_messages_to_file
from print_records import print_records_with_details
from search_record import search_record_by_substring
from update_file import *
from convert_txtFile_to_dictionary import get_record_dict


def insert_record(record_name, copies):
    try:
        records = get_record_dict()
        list_records = search_record_by_substring(record_name, records)
        old_copies = 0
        if len(list_records) > 1:
            print_records_with_details(records, list_records, index=True,new_record=True)
            option = ask_for_option_record(len(list_records) + 1,"add")
            if option < len(list_records) + 1:
                record_name = list_records[option - 1]
                old_copies = remove_line_from_file(list_records[option - 1])
        write_to_file(str(copies + old_copies) + ", " + record_name)
        log_messages_to_file("Insert", "Success")
        print(f"{record_name} record insertion succeed")
    except:
        log_messages_to_file("Insert", "Failure")
        print(f"{record_name} record insertion failed")



