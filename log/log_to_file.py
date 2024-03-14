import logging
import os


def log_messages_to_file(func_name, message , optinal = None):
    file_name = os.environ.get("file_name")
    log_filename = file_name + '_log.log'
    logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    if optinal != None:
        logging.info(str(func_name) + ' ' + str(message) + ' ' + optinal)
    else:
        logging.info(str(func_name) + ' ' + str(message))
