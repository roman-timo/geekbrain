# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс)
# этого проекта — одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся
# пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут
# быть обычные числа: V и H соответственно.

from abc import ABC, abstractmethod

class Cloth(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def amount(self):
        pass


class Coat(Cloth):
    @property
    def amount(self):
        return self.param / 6.5 + 0.5

class Suit(Cloth):
    @property
    def amount(self):
        return self.param * 2 + 0.3


coat1 = Coat(10)
suit1 = Suit(20)

print(coat1.amount + suit1.amount)
