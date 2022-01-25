# 1. Создать класс TrafficLight (светофор):
import time
from itertools import cycle

class TrafficLight:
    def __init__(self):
        self.__color = ['красный', 'желтый', 'зеленый']

    def running(self):
        for i in cycle(self.__color):
            self.__color = i
            print(i)
            if i == 'красный':
                time.sleep(7)
            elif i == 'желтый':
                time.sleep(2)
            else:
                time.sleep(5)

light1 = TrafficLight()
light1.running()
