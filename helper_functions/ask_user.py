def ask_for_option_record(option_range, remove_or_add):
    print(f"Choose the number of the record you want to {remove_or_add}", end=' ')
    if remove_or_add == "add":
        print(f",or add a new record by choosing number {option_range}")
    option = int(input())
    while not 0 < option <= option_range:
        option = int(input(f"Invalid selection. Please choose a number between 1 and {option_range}:"))
    return option
