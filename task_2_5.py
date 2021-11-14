
price_list = [57.8, 46.51, 97, 7.7, 7.05, 0.0]

for i,k in enumerate(price_list):
    price_list[i] = str(int(k)) + ' руб ' + f'{k:.2f}'[-2:] + ' коп'

# строка с разделением ", "
print(', '.join(price_list), ' | id =', id(price_list))

# сортировка по возрастанию
price_list.sort()
print(', '.join(price_list), ' | id =', id(price_list))

# сортировка по убыванию / новый список
new_price = sorted(price_list, reverse=True)
print(', '.join(new_price), ' | id =', id(new_price))

# 5 самых дорогих товаров - минимум кода!
print(price_list[-5:])

