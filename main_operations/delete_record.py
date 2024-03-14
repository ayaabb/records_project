from helper_functions import ask_user
from log.log_to_file import log_messages_to_file
from helper_functions.print_records import print_records_with_details
from main_operations.search_record import search_record_by_substring
from file_handle.update_file import *
from file_handle.convert_txtFile_to_dictionary import get_record_dict


def delete_record(record_name, copies):
    try:
        records = get_record_dict()
        record_name, old_copies, deleted = remove_record_to_overwrite(records, record_name,
                                                                      'remove', copies)
        if not deleted:
            raise Exception
        if old_copies != copies:
            write_to_file(record_name + ", " + str(old_copies - copies))
        log_messages_to_file("Delete", "Success")
        print(f"'{record_name}' record deleting succeed\n")

    except Exception as e:
        log_messages_to_file("Delete", "Failure")
        print(f"'{record_name}' record deleting failed\n")


def remove_record_to_overwrite(records, record_name, func_name, copies=0, new_record=False):
    # Search if there are any record with the given name
    list_records = search_record_by_substring(record_name, records)
    old_copies = 0
    # we found at least one record
    if len(list_records) > 1:
        print(f"Searching for '{record_name}' :")
        # print all the records that matches the search
        print_records_with_details(records, list_records, index=True, new_record=new_record)
        # ask the user which one he meant
        size = len(list_records)
        if func_name == 'add':
            size = len(list_records) + 1
        option = ask_user.ask_for_option_record(size, func_name)
        # he chose an item from the list
        if option <= len(list_records):
            record_name = list_records[option - 1]
            old_copies = records[record_name]
            if func_name == 'remove' and old_copies < copies:
                print('Not enough records to delete!')
                return record_name, old_copies, False
            remove_line_from_file(record_name)
    elif len(list_records) == 1:
        record_name = list_records[0]
        old_copies = records[record_name]
        if func_name == 'remove' and old_copies < copies:
            print('Not enough records to delete!')
            return record_name, old_copies, False
        remove_line_from_file(record_name)
    elif func_name != 'add':
        return record_name, old_copies, False
    return record_name, old_copies, True
