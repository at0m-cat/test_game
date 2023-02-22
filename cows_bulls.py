# -*- coding: utf-8 -*-


# В текущем модуле (lesson_006/mastermind.py) реализовать логику работы с пользователем:
#   модуль движка загадывает число
#   в цикле, пока число не отгадано
#       у пользователя запрашивается вариант числа
#       модуль движка проверяет число и выдает быков/коров
#       результат быков/коров выводится на консоль
#  когда игрок угадал таки число - показать количество ходов и вопрос "Хотите еще партию?"

from mastermind_engine import GenerateNumber, CheckNumber, GetNumber, SetNumber

GenerateNumber()
while True:
    number = input('Введите четырехзначное число: ')
    print('Вы ввели число {}'.format(number))
    if CheckNumber(number) is True:
        print('Проверяем количество быков и коров ...')
        SetNumber(number)
        print('ЧИСЛО ОТ ИИ ', GetNumber())
        continue

    # InputNum(number)
    # if CheckNumber(number) is False:
    #     print('asdsaaa: ___')
    #     continue
    #
    #
