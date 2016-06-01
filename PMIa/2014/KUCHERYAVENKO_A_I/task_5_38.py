# Задача 5. Вариант 38.
# Напишите программу, которая бы при запуске случайным образом
# отображала имя одной из семи птиц,
# доступных с первой версии игры Angry Birds. 
# Kucheryavenko A. I.
# 31.03.2016

import random

print("Программа случайным образом отображает имя одной из семи птиц,доступных с первой версии игры.")

birds = random.randint(1,7)
      
print('\nИмя птицы с первой версии игры', end=' ')

if birds == 1:
      print('Ред')
elif birds == 2:
      print('Джейк')
elif birds == 3:
      print('Чак')
elif birds == 4:
      print('Бомб')
elif birds == 5:
      print('Матильда')
elif birds == 6:
      print('Хэл')
elif birds == 7:
      print('Теренс')

input("\n\nНажмите Enter для выхода.")
