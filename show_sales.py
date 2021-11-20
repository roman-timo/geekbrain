# 7. * (вместо 6) Добавить возможность редактирования данных при помощи отдельного скрипта: передаём ему
# номер записи и новое значение. При этом файл не должен читаться целиком — обязательное требование.
# Предусмотреть ситуацию, когда пользователь вводит номер записи, которой не существует.

import sys

if len(sys.argv) == 2:
    start = int(sys.argv[1]) - 1
    end = None
elif len(sys.argv) == 3:
    start = int(sys.argv[1]) - 1
    end = int(sys.argv[2])
else:
    start = 0
    end = None

with open('bakery.csv', 'r', encoding='utf-8') as f:
    print(*f.readlines()[start:end])

