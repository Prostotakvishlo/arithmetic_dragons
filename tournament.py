# coding: utf-8
# license: GPLv3
from enemies import *
from hero import *

def annoying_input_int(message =''):
    answer = None
    while answer == None:
        try:
            answer = int(input(message))
        except ValueError:
            print('Вы ввели недопустимые символы')
    return answer
def annoying_input(message =''):
    answer=None
    while answer==None:
        try:
            answer=int(input(message))
        except ValueError:
            print('Вы ввели недопустимые символы')
    return answer
def game_tournament(hero, dragon_list):
    for dragon in dragon_list:
        print('Вышел', dragon._color, 'дракон!')
        while dragon.is_alive() and hero.is_alive():
            print('Вопрос:', dragon.question())
            answer = annoying_input_int('Ответ:')

            if dragon.check_answer(answer):
                hero.attack(dragon)
                print('Верно! \n** дракон кричит от боли **')
            else:
                dragon.attack(hero)
                print('Ошибка! \n** вам нанесён удар... **')
        if dragon.is_alive():
            break
        print('Дракон', dragon._color, 'повержен!\n')

    if hero.is_alive():
        print('Поздравляем! Вы победили!')
        print('Ваш накопленный опыт:', hero._experience)
    else:
        print('К сожалению, Вы проиграли...')

def game_tournament2(hero,troll_list):
    for troll in troll_list:
        print('Вышел',troll._color,'тролль!')
        while troll.is_alive() and hero.is_alive():
            print('Вопрос:',troll.question())
            answer=annoying_input('Ответ:')

            if troll.answer(answer):
                hero.attack(troll)
                print(' Верно \n** тролль кричит от боли')
                hero._experience+=1
            else:
                troll.attack(hero)
                print('Ошибка \n** вам нанесен удар')
        if troll.is_alive():
            break
        print('Тролль',troll._color,'побеждён!\n')
    if hero.is_alive():
        print('Победа!')
        print('Ваш накопленный опыт:',hero._experience,'\n')
    else:
        print('Вы проиграли!')
def start_game():

    try:
        print('Добро пожаловать в арифметико-ролевую игру с драконами!')
        print('Представьтесь, пожалуйста: ', end = '')
        hero = Hero(input())

        dragon_number = 3
        dragon_list = generate_dragon_list(dragon_number)
        assert(len(dragon_list) == 3)
        print('У Вас на пути', dragon_number, 'драконов!')
        game_tournament(hero, dragon_list)
        troll_number=1
        troll_list=generate_troll_list(troll_number)
        assert(len(troll_list)==1)
        print('У вас на пути',troll_number,'троллей!')
        game_tournament2(hero,troll_list)
    except EOFError:
        print('Поток ввода закончился. Извините, принимать ответы более невозможно.')
