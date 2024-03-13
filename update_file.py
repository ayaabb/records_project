import os
import os as o


def write_to_file(line):
    file_name = os.environ.get("file_name")
    if not o.path.isfile(file_name):
        with open(file_name, "w") as file:
            file.writelines(line + '\n')
    else:
        with open(file_name, "a") as file:
            file.writelines(line + '\n')


def remove_line_from_file(name_to_delete):
    file_name = os.environ.get("file_name")

    with open(file_name, "r") as file:
        lines = file.readlines()
    modified_lines = []
    file_copies = 0
    for line in lines:
        line_split = (line.strip()).split(' ,')
        if name_to_delete == line_split[1]:
            file_copies = int(line_split[0])
        else:
            modified_lines.append(line)
    with open(file_name, "w") as output:
        output.writelines(modified_lines)
    return file_copies
