# 4. * (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки
# в формате «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари,
# реализованные по схеме предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы.


def names_dict(surname, *args):
    """Создает словарь по Имени или Фамилии, в зависимости от аргумента surname"""

    my_dict = {}
    for i in args:

        if surname:
            key_name = i.split()[1][0]
        else:
            key_name = i[0]

        if key_name in my_dict:
            my_dict[key_name].append(i)
        else:
            my_dict[key_name] = [i]

    return my_dict


def thesaurus_adv(*args):
    """сначала создает словарь по фамилии, затем в нем словарь по имени для каждого элемента"""

    my_dict = names_dict(True, *args)
    for keys, vals in my_dict.items():
        my_dict[keys] = names_dict(False, *vals)

    return my_dict


out_dict = thesaurus_adv("Иван Сергеев", "Петр Алексеев", "Ипполит Корнеев", "Акоп Сергеев", "Акопян Корнев", "Иннокентий Сапожков")

# без сортировки
for i,k in out_dict.items():
    print(i, k)

print('---------сортировка----------')

# с сортировкой
for i,k in sorted(out_dict.items()):
    print(i, k)

# print(dict(sorted(out_dict.items())))
