# -*- coding: utf-8 -*-


# В текущем модуле (lesson_006/mastermind.py) реализовать логику работы с пользователем:
#   модуль движка загадывает число
#   в цикле, пока число не отгадано
#       у пользователя запрашивается вариант числа
#       модуль движка проверяет число и выдает быков/коров
#       результат быков/коров выводится на консоль
#  когда игрок угадал таки число - показать количество ходов и вопрос "Хотите еще партию?"

from mastermind_engine import GenerateNumber, CheckNumber, GetNumber

GenerateNumber()
while True:
    number = input('Введите четырехзначное число: ')
    print('Вы ввели число {}'.format(number))
    print('Проверяем количество быков и коров ...')
    print(GetNumber())
    CheckNumber(number)
    if CheckNumber(number) is False:
        print('asdsaaa: ___')
        break



