def print_records_with_details(records, list_names, index=False, copies=False, new_record=False):
    print("These results founded:")
    if not index and copies:
        """Search function"""
        for name in list_names:
            print(f"Record name: {name} , Amount = {records[name]}")
    elif index:
        """Delete , update_name and update_record functions"""
        for i in range(len(list_names)):
            print(f"{i + 1}){list_names[i]}")

        if not copies and new_record:
            """Insert function"""
            print(f"{len(list_names) + 1})New record")
