# 5. *(вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи те же, а значения — кортежи вида (<files_quantity>, [<files_extensions_list>]), например:

import os
import json
from collections import defaultdict


folder = r'C:\Users\roman\PycharmProjects\myfirstPyproject'
file_count = defaultdict(int)
ext_count = defaultdict(set)
final_count = {}

for root, dirs, files in os.walk(folder):
    for file in files:
        file_size = os.stat(os.path.join(root, file)).st_size
        ext = file.rsplit('.', maxsplit=1)[-1].lower()
        file_count[10 ** len(str(file_size))] += 1
        ext_count[10 ** len(str(file_size))].add(ext)

for key, val in file_count.items():
    final_count[key] = (val, list(ext_count[key]))

with open(f'{os.path.basename(folder)}_summary', 'w', encoding='utf-8') as f:
    f.write(json.dumps(final_count))


print(sorted(final_count.items()))