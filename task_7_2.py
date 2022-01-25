# 2. *(вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:

import os

root = r'Task_7_2'
folder_list = []
level = 0

with open('config.yaml', encoding='utf-8') as src:
    for line in src:
        if line.strip()[-1] == ':':
            if line.count(' ') > level:
                os.mkdir(os.path.join(root, line.strip()[:-1]))
                root = os.path.join(root, line.strip()[:-1])
            elif line.count(' ') < level:
                for _ in range(int((level - line.count(' ')) / 3)+1):
                    root = os.path.dirname(root)
                os.mkdir(os.path.join(root, line.strip()[:-1]))
                root = os.path.join(root, line.strip()[:-1])
            elif line.count(' ') == level:
                root = os.path.join(os.path.dirname(root), line.strip()[:-1])
                os.mkdir(root)
            level = line.count(' ')

        if line.count(' - '):
            with open(os.path.join(root, line.strip()[2:]), 'w', encoding='utf-8') as f:
                f.write('empty file')
