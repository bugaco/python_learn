from random import randint
import random

class Die():
    def __init__(self, sides=6):
        """init方法，默认sides为6"""
        self.sides = sides

    def roll_die(self):
        """滚动骰子"""
        side = randint(1, self.sides)
        print(side)

my_die_10 = Die(10)
count = 0
while count < 10:
    my_die_10.roll_die()
    count+=1
print('分割线－－－－－－🐯')
my_die_20 = Die(20)
count = 0
while count < 10:
    my_die_20.roll_die()
    count+=1

