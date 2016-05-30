# Задача 7. Вариант 30.
# Создайте игру, в которой компьютер загадывает название одного из двенадцати
# месяцев, а игрок должен его угадать.


# Khasanova I. F.
# 14.04.2016

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


trial = 11
bonus = 11000

while trial > 0 :
    answer = input('\nКак Вы думаете, какой месяц загадан? ')
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

		
input("\n\nНажмите Enter для выхода.")
