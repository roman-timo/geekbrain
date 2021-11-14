# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх списков (по одному из каждого):

from copy import copy

from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(n, repeat):
    """
    Функция возвращает n строк, по одному слову из каждого списка.
    Слова повторяются, если repeat = True; не повторяются, если repeat = False
    """
    out_string = []
    nouns_copy, adv_copy, adj_copy = copy(nouns), copy(adverbs), copy(adjectives)

    for i in range(n):
        new_noun, new_adv, new_adj = choice(nouns_copy), choice(adv_copy), choice(adj_copy)
        out_string.append(f'{new_noun} {new_adv} {new_adj}')
        if repeat == False:
            nouns_copy.remove(new_noun)
            adv_copy.remove(new_adv)
            adj_copy.remove(new_adj)
    return out_string


print(get_jokes(5, repeat=False))