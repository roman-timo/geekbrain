# ДЗ 1_2 - кубы нечетных чисел

cube_list = []
total_seven = 0
total_seven2 = 0

for i in range(1,1000,2):
    cube_list.append(i**3)

    # задание а)
    sum_digits = 0
    for k in range(len(str(i**3))):
            sum_digits += int(str(i**3)[k])
    if sum_digits % 7 == 0:
        total_seven += i**3

    # задание b)
    sum_digits = 0
    for k in range(len(str(i**3 + 17))):
            sum_digits += int(str(i**3 + 17)[k])
    if sum_digits % 7 == 0:
        total_seven2 += i**3 + 17


print(cube_list)
print(total_seven)
print(total_seven2)
