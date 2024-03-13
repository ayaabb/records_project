import os
import sys

from search_record import *
from update_copies_record import update_copies


def main():
   pass


if __name__ == '__main__':
    external_param = sys.argv[1]
    os.environ["file_name"] = external_param

    main()
