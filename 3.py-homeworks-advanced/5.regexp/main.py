from work_class import work_with_files, parsing

if __name__ == "__main__":
    raw_data_path = "initial_data/phonebook_raw.csv"
    raw_contact_list = work_with_files.get_row(raw_data_path)

    dirty_contact_list = parsing.data_processing(raw_contact_list)
    clear_contact_list = parsing.clear_contact_list(dirty_contact_list)

    clear_list_path = "initial_data/phonebook_new.csv"
    work_with_files.save_new(clear_contact_list, clear_list_path)