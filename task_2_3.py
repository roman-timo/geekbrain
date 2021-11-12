# 3. * (вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place). Эта задача намного серьёзнее, чем может сначала показаться.


original_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i, k in enumerate(original_list):
    if k[-1].isdigit() and original_list[i-1] != '"*':

        if k[0] == '+' or k[0] == '-':
            sign = k[0]
        else:
            sign = ''

        original_list[i] = f'{sign}{abs(int(k)):02d}'
        original_list.insert(i, '"*')
        original_list.insert(i+2, '*"')

print(' '.join(original_list).replace('"* ', '"').replace(' *"', '"'))