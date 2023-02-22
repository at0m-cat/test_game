# -*- coding: utf-8 -*-
import mastermind_engine
from mastermind_engine import GenerateNumber, CheckNumber, GetNumber, SetNumber

GenerateNumber()
while True:
    number = input('Введите четырехзначное число: ')
    print('Вы ввели число {}'.format(number))
    if CheckNumber(number) is True:
        print('Проверяем количество быков и коров ...')
        SetNumber(number)
        print(mastermind_engine._animals)
        # print('ЧИСЛО ОТ ИИ ', GetNumber())
        if mastermind_engine.BULL == 4:
            print('МОЛОДЕЦ, МАЛОЙ! Победил за {} ходов'
                  .format(mastermind_engine._counter))
            print('Еще партию? Y/N:')
            _ = input()
            if _ == 'Y':
                GenerateNumber()
                mastermind_engine._counter = 0
                continue
            if _ == 'N':
                break
    continue
