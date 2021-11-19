# 5. Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.

import sys

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

src2_list = [i for i in src if src.count(i) == 1]
src2_tup = (i for i in src if src.count(i) == 1)

print(src2_list, sys.getsizeof(src2_list))
# оптимизация по памяти - лучше генератор (?)
print(list(src2_tup), sys.getsizeof(src2_tup))
