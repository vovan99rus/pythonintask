# Задача 6. Вариант 48.
# Создайте игру, в которой компьютер загадывает название одной из двадцати
# башен Московского кремля, а игрок должен его угадать.

# Vinogradova J.
# 31.03.2016

import random
name = random.randint(1,12)

    
if name == 1 :
    name = 'Беклемишевская'
elif name == 2 :
    name = 'Константино-Еленинская'
elif name == 3 :
    name = 'Набатная'
elif name == 4 :
    name = 'Царская'
elif name == 5 :
    name = 'Спасская'
elif name == 6 :
    name = 'Сенатская'
elif name == 7 :
    name = 'Никольская'
elif name == 8 :
    name = 'Собакина'
elif name == 9 :
    name = 'Граненая'
elif name == 10 :
    name = 'Троицкая'
elif name == 11 :
    name = 'Кутафья'
elif name == 12 :
    name = 'Комендатская'
elif name == 13 :
    name = 'Оружейная'
elif name == 14 :
    name = 'Боровицкая'
elif name == 15 :
    name = 'Водовзводная'
elif name == 16 :
    name = 'Благовещенская'
elif name == 17 :
    name = 'Тайницкая'
elif name == 18 :
    name = 'Первая Безымянная'
elif name == 19 :
    name = 'Вторая Безымянная'
else :
    name = 'Петровская'
trial = 19
bonus = 11000

while trial > 0 :
    answer = input('\nКак Вы думаете, какая башня загадана? ')
    if answer == name :
        print('\nВы угадали!')
        print('Вам начислено', bonus, 'баллов.')
        break
    else :
        print('\nВы не угадали!!!')
        if trial > 1 :
            print('Попробуйте еще раз.')
        else :
            print('Правильный ответ: ', name)
        
    trial -= 1
    bonus -= 1000
input('\n\nНажмите Enter для выхода.')
