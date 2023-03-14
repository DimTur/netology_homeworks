import re

phone_search_pattern = r"(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*"
phone_sub_pattern = r"+7(\2)\3-\4-\5 \6\7"


def data_processing(data):
    total = list()
    for row in data:
        note = list()
        full_name = re.findall(r"(\w+)", " ".join(row[:3]))
        full_name.append("") if len(full_name) < 3 else ...
        note += full_name
        note.append(row[3])
        note.append(row[4])
        note.append(re.sub(phone_search_pattern, phone_sub_pattern, row[5]).strip())
        note.append(row[6])
        total.append(note)
    return total


def clear_contact_list(data):
    total = dict()
    for part in data:
        total[part[0]] = merge_duplicates(part, total[part[0]]) if part[0] in total else part
    return total.values()


def merge_duplicates(note1, note2):
    total = list()
    for index in range(len(note1)):
        total.append(note1[index]) if note1[index] else total.append(note2[index])
    return total
