# 3. Есть два списка: Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>)

from itertools import zip_longest

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А'
]

out_cort = ((tutor, klass) for tutor, klass in zip_longest(tutors, klasses))

print(*out_cort, sep='\n')
