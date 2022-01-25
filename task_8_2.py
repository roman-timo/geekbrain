# 2. *(вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt

import re

RE_PARSE = re.compile(r'(\d+\.\d+\.\d+\.\d+)\ - - \[(...+)]\ \"(\w+)\ (...+)\ HTTP/1.1\" (\d+)\ (\d+)')

with open('nginx_logs.txt', encoding='utf-8') as f:
    for line in f:
        if RE_PARSE.match(line):
            print(RE_PARSE.findall(line))
        else:
            raise ValueError('Wrong line -', {line})

