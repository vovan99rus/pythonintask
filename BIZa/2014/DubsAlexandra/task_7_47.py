# Задача 7. Вариант 47
# Создайте игру, в которой компьютер загадывает название одной из двенадцати линий московского метрополитена, а игрок должен его угадать.
# Чем меньше попыток Вы используете, тем больше баллов заработаете

# Dubs A. E.
# 20.04.2016

import random

print ("Программа случайным образом загадывает название одного из одной из двенадцати линий московского метрополитена, а игрок должен его угадать.")
print ("Чем меньше попыток Вы используете, тем больше баллов заработаете")

lines = ('Сокольническая','Замоскворецкая','Арбатско-Покровская','Филевская','Кольцевая','Калужско-Рижская','Таганско-Краснопресненская','Серпуховско-Тимирязевская','Калининская','Люблинско-Дмитровская','Каховская','Бутовская')

comp_variant = random.choice(lines)

print ("\n Назовите одну из линий линий московского метрополитена ")

popitki = 0 
ball = 100

while popitki < 5:
	my_variant = input (' Ваш ответ: ')
	popitki = popitki + 1
	ball = ball - 20

	if my_variant == comp_variant:
		print (" \n Вы выиграли! \n Число попыток: ", popitki, "\n У Вас  очков", ball)
	else:
		print (" \n Вы поиграли! Попробуйте еще раз ",  "\n Число попыток: " , popitki, "\n У Вас  очков", ball)

input ("\n\n Нажмите Enter для выхода.")