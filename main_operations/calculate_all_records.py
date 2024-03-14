from log.log_to_file import log_messages_to_file
from file_handle.convert_txtFile_to_dictionary import *


def calculate_records_num():
    records = get_record_dict()
    amount = 0
    for record,copies in records.items():
        amount += copies
    
    if amount <= 0:
        print("There are no records yet!")
    else:
        log_messages_to_file("Print Amount", amount)

