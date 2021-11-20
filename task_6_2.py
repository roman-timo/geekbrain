# 2. * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным
# файла логов из предыдущего задания.

spam_list = ()
top_dict = {}
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        spam_list = line.split()[0], line.split()[5], line.split()[6]
        if top_dict.get(line.split()[0]) != None:
            top_dict[line.split()[0]] += 1
        else:
            top_dict[line.split()[0]] = 1


#  сортировка словаря

for i in range(5):
    print(sorted(top_dict.items(), reverse=True, key=lambda x: x[1])[i])

