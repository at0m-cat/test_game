# -*- coding: utf-8 -*-
from random import randint

COW, BULL = None, None,
_number = None
_animals = {}


def GenerateNumber():
    global _number
    generator = set()
    _number = ''
    while True:
        generator.add(str(randint(1, 9)))
        if len(generator) == 4:
            break
    for value in generator:
        _number += str(value)


def GetNumber():
    return int(_number)


def CheckNumber(supposed_number):
    global COW, BULL, _animals
    _animals, COW, BULL = {}, 0, 0
    while CheckNumber is False:
        return 0

    if len(str(supposed_number)) != 4:
        print('ERROR !!!')
        return False

# Чтобы не повторялись числа при вводе, можно использовать систему множеств. После ввода
# пользователем числа, его длина должна быть 4, в противном случае ввести снова число.

    while supposed_number:
        bunch_number_user, bunch_number_generate = set(), set()
        user_num, server_num = [], []
        for i, j in enumerate(str(supposed_number)):
            bunch_number_user.add(j)
            user_num.append(int(j))
        for i, j in enumerate(_number):
            bunch_number_generate.add(j)
            server_num.append(int(j))
        for i in range(0, 4):
            if server_num[i] - user_num[i] == 0:
                BULL += 1
        COW = len(bunch_number_user & bunch_number_generate)
        if BULL:
            COW = COW - BULL
        _animals['bulls'] = BULL
        _animals['cows'] = COW
        print(_animals)
        supposed_number = False

