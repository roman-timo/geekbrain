# 2. Реализовать класс Road (дорога).


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def vol(self):
        return self._length * self._width * 25 * 5 / 1000


road1 = Road(2, 3)
print(road1.vol(), 'т')
