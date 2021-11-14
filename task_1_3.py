# Задание 3 - процентх

for i in range(100):

    if str(i + 1)[-1] == '1':
        ending = ''
    elif str(i + 1)[-1] == '2' or str(i + 1)[-1] == '3' or str(i + 1)[-1] == '4':
        ending = 'а'
    else:
        ending = 'ов'

    if (i + 1) // 10 == 1:
        ending = 'ов'

    print(i + 1, 'процент' + ending)

#end
