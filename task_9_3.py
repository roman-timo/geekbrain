# 3. Реализовать базовый класс Worker (работник):

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)
    def get_total_income(self):
        print(self._income['wage'] + self._income['bonus'])

person1 = Position('Ivan', 'Petrov', 'Worker', 100, 20)
person1.get_full_name()
person1.get_total_income()