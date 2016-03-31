# Задача 7. Вариант 23
# Создайте игру, в которой компьютер загадывает название одного 
# из семи дней недели, а игрок должен его угадать.

# Moshkov Y. O.
# 31.03.2016

import random
week = ["Понедельник", "Вторник", "Среда", 
"Четверг", "Пятница", "Суббота", "Воскресенье"]
number = random.randint(0, 6)
day = week[number].lower()

inputDay = input("Угадайте один из семи дней недели: ")
score = 6
while inputDay != day:
	out = "Ваш счёт " + score + "Вы не угадали, попробуйте ещё раз: "
	inputDay = input(out)
	score = score - 1
out += " Нажмите Enter для выхода."
input(out)