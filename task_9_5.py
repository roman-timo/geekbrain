# 5. Реализовать класс Stationery (канцелярская принадлежность):

class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationary):
    def draw(self):
        print('Запуск отрисовки Pen')
class Pencil(Stationary):
    def draw(self):
        print('Запуск отрисовки Pencil')
class Handle(Stationary):
    def draw(self):
        print('Запуск отрисовки Handle')

pen1 = Pen('pen1')
pen1.draw()
