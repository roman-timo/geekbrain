# 1. Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя
# и почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение ValueError.

import re

raw = 'email@domain.ru'

RE_EMAIL = re.compile(r'(?P<user>^[a-zA-Z\d]+)\@(?P<domain>[a-zA-Z\d]+\.[a-zA-Z\d]+)$')

if RE_EMAIL.match(raw):
    print(*map(lambda x: x.groupdict(), RE_EMAIL.finditer(raw)))
else:
    raise ValueError(f'wrong email: {raw}')
