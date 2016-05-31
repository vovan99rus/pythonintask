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
otvet = input('Как Вы думаете, какая башня загадана?')
if name == otvet:
    print ('Верно')
else:
    print ('Неверно')
    print('Правильный ответ: ', name)
input('\n\nНажмите Enter для выхода.')
