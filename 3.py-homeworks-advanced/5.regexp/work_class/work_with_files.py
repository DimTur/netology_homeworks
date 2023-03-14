import csv

def get_row(raw_data_path):
    with open(raw_data_path, encoding="utf-8") as csv_file:
        rows = csv.reader(csv_file, delimiter=",")
        contacts_list = list(rows)
    return contacts_list


def save_new(data, new_data_path):
    with open(new_data_path,"w", encoding="utf-8", newline="") as csv_file:
        writer = csv.writer(csv_file, delimiter=",")
        writer.writerows(data)