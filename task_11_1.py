# == Лото ==
# Правила игры в лото.
# Игра ведется с помощью спе циальных карточек, на которых отмечены числа,
# и фишек (бочонков) с цифрами.

import random
from random import shuffle


class LotoCard:
    def __init__(self, name):
        self.name = name
        self.cardnum = []
        randlist = [i + 1 for i in range(90)]
        shuffle(randlist)
        self.cardnum += sorted(randlist[0:5])
        self.cardnum += sorted(randlist[5:10])
        self.cardnum += sorted(randlist[10:15])

    def __str__(self):
        printcard = []
        outstr = ''
        printcard.append(self.cardnum[0:5])
        printcard.append(self.cardnum[5:10])
        printcard.append(self.cardnum[10:15])

        for i in range(3):
            for j in range(4):
                printcard[i].insert(random.randint(0,len(printcard[i])), ' ')

        for i, val_i in enumerate(printcard):
            for j, val_j in enumerate(val_i):
                outstr += str(printcard[i][j]) + ' '
            outstr += '\n'

        return f'{self.name}\n' + outstr

    def checknum(self, num):
        if num in self.cardnum:
            self.cardnum[self.cardnum.index(num)] = '-'
            return True
        else:
            return False

    def iswin(self):
        return self.cardnum.count('-') == len(self.cardnum)

class LotoGame:
    def __init__(self, pl1, pl2):
        self.pl1 = pl1
        self.pl2 = pl2

    def start(self):
        num_set = []
        wrongchoice = False
        num_set = [i + 1 for i in range(90)]
        shuffle(num_set)

        while num_set \
                and not wrongchoice \
                and not self.pl1.iswin() \
                and not self.pl2.iswin():

            show_num = num_set.pop()
            print(f'Новый бочонок:{show_num} (осталось {len(num_set)})')

            # choice = input('Зачеркнуть цифру? (y/n) ')
            # wrongchoice = (self.pl1.checknum(show_num) and choice == 'n') \
            #                 or (not self.pl1.checknum(show_num) and choice == 'y')

            self.pl1.checknum(show_num)
            self.pl2.checknum(show_num)
            print(self.pl1)
            print(self.pl2)

        else:
            winnername = (self.pl1.name * self.pl1.iswin()) or (self.pl2.name * self.pl2.iswin())
            print(f'Выиграл:', winnername)



player1 = LotoCard('Игрок 1')
player2 = LotoCard('Компьютер')

game1 = LotoGame(player1, player2)

print(player1)
print(player2)
game1.start()

