#Задача 6. Вариант 3
#Программа, в которой компьютер загадывает имя одной из семи птиц, доступных с первой версии игры Angry Birds, а игрок должен его угадать.

#Байбулатова К.В.
#21.03.2016

import random 
AngryBirds=('Ред','Чак','Матильда','Теренс','Бабблз','Стелла','Тони')
name=random.randint(0,6)
rand=AngryBirds[name]
print('Компьютер загадал имя одной из семи птиц, доступных с первой версии игры Angry Birds')
#print(rand)
otvet=0
while(otvet)!=(rand):
        otvet= input('Введите имя одной из птиц Angry Birds:')
        if (otvet)!=(rand):
                print('Вы не угадали. Попробуйте еще раз')
        elif(otvet)==(rand):
                print('Вы угадали!Поздравляю!')
                break
input('Нажмите Enter для выхода')		
