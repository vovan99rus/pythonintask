Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Задача 5. Вариант 50
# Напишите программу, которая бы при запуске случайным образом отображала 
# имя одной из трех официальных жен Зевса.

# Bronnikov I. S.
# 25.05.2016

import random
wifes = ["Пики", "Крести", "Черви", "Бубны"]
number = random.randint(0, 3)
name = wifes[number]

print(name, "- масть франзуцкой карточной колоды")
input("\nНажмите Enter для выхода.")


