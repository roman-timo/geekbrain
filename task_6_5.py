# 5. ** (вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было задать путь к обоим
# исходным файлам и путь к выходному файлу со словарём. Проверить работу скрипта для случая, когда все файлы
# находятся в разных папках.

import json
from itertools import zip_longest
import json
import sys

#  для задачи 3
# with open('users.csv', 'r', encoding='utf-8') as f:
#     name_list = f.read()
# with open('hobby.csv', 'r', encoding='utf-8') as f:
#     hobby_list = f.read()

name_list = []
hobby_list = []
name_dict = {}

# Поскольку условие, что файл больше ОЗУ, то нужно читать и Сохранять построчно:

with open(sys.argv[1], 'r', encoding='utf-8') as f:
    with open(sys.argv[2], 'r', encoding='utf-8') as f2:
        for line in f:
            name_list = line.split(',')
            hobby_list = f2.readline().strip()
            if hobby_list == '':
                hobby_list = None

            name_dict['Фамилия'] = name_list[0].strip()
            name_dict['Имя'] = name_list[1].strip()
            name_dict['Отчество'] = name_list[2].strip()
            name_dict['Хобби'] = hobby_list

            with open(sys.argv[3], 'a', encoding='utf-8') as f_out:
                f_out.writeline(f'{str(name_dict)}\n')

        # обработка ошибки, если hobby длиннее, чем users
        if f2.readline() != '':
            exit(1)


print(name_dict)

# dict_out = dict(zip_longest(name_list.split('\n'),hobby_list.split('\n')))
#
# with open('file_dict.json', 'w', encoding='utf-8') as f:
#     f.write(json.dumps(dict_out))


