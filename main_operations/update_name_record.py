from log.log_to_file import log_messages_to_file
from file_handle.update_file import *
from file_handle.convert_txtFile_to_dictionary import get_record_dict
from main_operations.delete_record import *


def update_name(old_name, new_name):
    try:
        records = get_record_dict()
        record_name , old_copies ,updated =remove_record_to_overwrite(records,old_name,'update')
        if updated == False:
            print("Record name doesn't found")
            raise Exception
       
        write_to_file(new_name + ", " + str(old_copies))
        log_messages_to_file("Update name", "Success")
        print(f"{record_name} record name update succeed")
        
            
    except Exception as e:
        log_messages_to_file("Update name", "Failure")
        print(f"{old_name} record name update failed")
