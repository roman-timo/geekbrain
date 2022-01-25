# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.

class Matrix:
    def __init__(self, mx_list):
        self.mx = mx_list

    def __str__(self):
        out_mx = ''
        for row in self.mx:
            out_mx = out_mx + f'{" ".join(map(str, row))}\n'
        return f'{out_mx}'

    def __add__(self, other):
        try:
            for i, val_i in enumerate(self.mx):
                for j, val_j in enumerate(val_i):
                     self.mx[i][j] += other.mx[i][j]
            return self
        except IndexError:
            print('wrong matrix size!')


mx_raw1 = \
[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

mx_raw2 = \
[
    [9,8,7],
    [6,5,4],
    [3,2,1]
]


mx1 = Matrix(mx_raw1)
mx2 = Matrix(mx_raw2)


mx3 = mx1 + mx2
print(mx3)

