import os


def create_new_file(directory):
    file_list = os.listdir(directory)
    new_list = []

    for file in file_list:
        with open(directory + "/" + file, encoding='utf-8') as cur_file:
            new_list.append([file, 0, []])
            for line in cur_file:
                new_list[-1][2].append(line.strip())
                new_list[-1][1] += 1

    return sorted(new_list, key=lambda x: x[2], reverse=True)


def create_file_from_directory(directory, filename):
    with open(filename + '.txt', 'w+') as newfile:
        for file in create_new_file(directory):
            newfile.write(f'File name: {file[0]}\n')
            newfile.write(f'Length: {file[1]} string(s)\n')
            for string in file[2]:
                newfile.write(string + '\n')
            newfile.write('***********************\n')


create_file_from_directory('text', 'new_text')