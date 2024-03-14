from log.log_to_file import log_messages_to_file
from file_handle.update_file import *
from file_handle.convert_txtFile_to_dictionary import get_record_dict
from main_operations.delete_record import *



def update_copies_in_records( record_name, new_copies):
    try:
        records = get_record_dict()
        record_name , old_copies ,updated =remove_record_to_overwrite(records,record_name,'update')
        if updated == False:
            print("Record name doesn't found")
            raise Exception

    
        write_to_file(record_name + ", " + str(new_copies))
        log_messages_to_file("Update copies", "Success")
        print(f"{record_name} record copies update succeed")
       
    except:
        log_messages_to_file("Update copies", "Failure")
        print(f"{record_name} record copies update failed")


def update_copies():
    pass
