# 3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates, например:

import os
from shutil import copytree

folder = r'C:\Users\roman\PycharmProjects\myfirstPyproject\venv\Task_7\my_project'
templ_fold = os.path.join(folder, 'templates')

try:
    for root, dirs, files in os.walk(folder):
        if os.path.basename(root) == 'templates' and os.path.dirname(root) != folder:
            for _ in os.listdir(root):
                copytree(os.path.join(root, _), os.path.join(templ_fold, _))
except WindowsError as e:
    print(f'Ошибка - папка уже существует:\n{e}')


