# Задача 6. Вариант 30.
# Создайте игру, в которой компьютер загадывает название одного из двенадцати
# месяцев, а игрок должен его угадать.

# Khasanova I. F.
# 31.03.2016

import random
name = random.randint(1,12)

    
if name == 1 :
    name = 'Январь'
elif name == 2 :
    name = 'Февраль'
elif name == 3 :
    name = 'Март'
elif name == 4 :
    name = 'Апрель'
elif name == 5 :
    name = 'Май'
elif name == 6 :
    name = 'Июнь'
elif name == 7 :
    name = 'Июль'
elif name == 8 :
    name = 'Август'
elif name == 9 :
    name = 'Сентябрь'
elif name == 10 :
    name = 'Октябрь'
elif name == 11 :
    name = 'Ноябрь' 
else :
    name = 'Декабрь'
otvet = input('Как Вы думаете, какой месяц загадан?')
if name == otvet:
    print ('Верно')
else:
    print ('Неверно')
    print('Правильный ответ: ', name)
input('\n\nНажмите Enter для выхода.')
