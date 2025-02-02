import os


def len_file(file_path_):
    with open(file_path_, encoding='utf-8') as f:
        lines = f.readlines()
        len_ = len(lines)
    return len_


BASE_PATH = os.getcwd() + ('/sorted')
list_dir = os.listdir(BASE_PATH)
list_dir.remove('combine.txt')

dict_files = dict()
for i in list_dir:
    dict_files[str(i)] = len_file(os.path.join(BASE_PATH, str(i)))

combine_path = os.path.join(BASE_PATH, 'combine.txt')

# Создать/перезатереть файл
with open(combine_path, 'w', encoding='utf-8') as combine:
    combine.write(f'')

for file_info in sorted(dict_files.items(), key=lambda x: x[1]):
    with open(combine_path, 'a') as c_:
        c_.write(f'{file_info[0]}\n')
        c_.write(f'{file_info[1]}\n')
    with open(os.path.join(BASE_PATH, file_info[0]), encoding='utf-8') as f_:
        data = f_.read()
    with open(combine_path, 'a') as c_:
        c_.write(f'{data.strip()}\n\n')

with open(combine_path) as c_:
    data = c_.read()
print(data)