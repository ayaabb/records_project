import os
import sys

from search_record import *
from update_copies_record import update_copies


def main():
    text_number_dictionary = {
        "apple pie": 5,
        "banana tree": 10,
        "orange good vibes": 7,
        "grape": 3,
        "kiwi": 8
    }


if __name__ == '__main__':
    external_param = sys.argv[1]
    os.environ["file_name"] = external_param

    # main()
