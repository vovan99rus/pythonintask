#Задача 5. Вариант 24
#Напишите программу, которая бы при запуске случайным образом отображала название одной из шести шахматных фигур.

#Semyenov A.N.
#28.03.2016
print("Программа выводит на экран название одной из шести шахматных фигур.")
import random
a = random.choice(['король', 'пешка', 'ферзь', 'ладья', 'конь', 'слон'])
print (a)
input("\nНажмите Enter для выхода")