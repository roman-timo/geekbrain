# 4. Реализуйте базовый класс Car:

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        pring('go')
    def stop(self):
        print('stop')
    def turn(self, direction):
        print('turn', direction)
    def show_speed(self):
        print(self.speed)

class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('high speed')
class SportCar(Car):
    pass
class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('high speed')
class PoliceCar(Car):
    pass

towncar1 = TownCar(70, 'красный', 'towncar1', False)
towncar1.show_speed()
towncar1.turn('right')
