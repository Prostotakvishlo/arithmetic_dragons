# coding: utf-8
# license: GPLv3
from gameunit import *
from random import randint, choice

class Enemy(Attacker):
    pass


def generate_random_dragon():
    RandomDragonType=choice(dragon_types)
    dragon=RandomDragonType()
    return dragon
def generate_random_troll():
    RandomTrollType=choice(troll_types)
    troll=RandomTrollType()
    return troll
def generate_dragon_list(enemy_number):
    enemy_list = [generate_random_dragon() for i in range(enemy_number)]
    return enemy_list
def generate_troll_list(troll_number):
    enemy_list=[generate_random_troll() for i in range (troll_number)]
    return enemy_list
class Dragon(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer


class GreenDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'зелёный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '+' + str(y)
        self.set_answer(x + y)
        return self.__quest

class RedDragon(Dragon):
    def __init__(self):
        self._health=20
        self._attack=1
        self._color='красный'
    def question(self):
        x=randint(1,10)
        y=randint(1,10)
        self.__quest=str(x)+'-'+str(y)
        self.set_answer(x-y)
        return self.__quest
class BlackDragon(Dragon):
    def __init__(self):
        self._health=20
        self._attack=1
        self._color='чёрный'
    def question(self):
        x=randint(1,10)
        y=randint(1,10)
        self.__quest=str(x)+'*'+str(y)
        self.set_answer(x*y)
        return self.__quest
class Troll(Enemy):
    def set_answer(self,answer):
        self._answer=answer
    def check_simplicity(self,n):
        for i in range(2,n//2):
            if n%i==0:
                return 'NO'
        return 'YES'
    def answer(self,answer):
        return answer==self.answer
class Troll1(Troll):
    def __init__(self):
        self.x=randint(1,5)
        self._health=5
        self._attack=1
        self._color='интересный'
    def question(self):
        self.set_answer(str(self.x))
        self._quest='Угадай число!'
        return self._quest
dragon_types=[GreenDragon, RedDragon, BlackDragon]
troll_types=[Troll1]