# 2. * (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с
# числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:


def num_translate_adv(rus_num):
    """Функция переводит числительные англ -> рус"""

    dict = {'zero': 'ноль',
               'one': 'один',
               'two': 'два',
               'three': 'три',
               'four': 'четыре',
               'five': 'пять',
               'six': 'шесть',
               'seven': 'семь',
               'eight': 'восемь',
               'nine': 'девять',
               'ten': 'десять',}
    result = dict.get(rus_num.lower())
    if rus_num.istitle() and result != None:
        result = result.title()
    return result


what_num = input('введите число на английском: ')
print(num_translate_adv(what_num))