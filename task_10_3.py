# 3. Осуществить программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс «Клетка».
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). В классе должны
# быть реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение
# (__mul__()), деление (__floordiv____truediv__()). Эти методы должны применяться только к клеткам и выполнять
# увеличение, уменьшение, умножение и округление до целого числа деления клеток соответственно.


class Cell:
    def __init__(self, cellnum):
        self.cellnum = cellnum

    def __str__(self):
        return str(self.cellnum)

    def __add__(self, other):
        return Cell(self.cellnum + other.cellnum)

    def __sub__(self, other):
        return Cell(self.cellnum - other.cellnum) if self.cellnum >= other.cellnum \
            else print('Первых клеток меньше, чем вторых')

    def __mul__(self, other):
        return Cell(self.cellnum * other.cellnum)

    def __floordiv__(self, other):
        return Cell(self.cellnum // other.cellnum)

    def make_order(self, rownum):
        cellstr = ''
        for i in range(self.cellnum // rownum):
            cellstr += '*' * rownum + '\n'
        cellstr += '*' * (self.cellnum % rownum)
        return cellstr


cell1 = Cell(5)
cell2 = Cell(3)
cell3 = cell1 + cell2
print(cell3)
cell3 = cell1 - cell2
print(cell3)
cell3 = cell1 * cell2
print(cell3)
cell3 = cell1 // cell2
print(cell3)
print(cell1.make_order(3))