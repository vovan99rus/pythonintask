# Задача 7. Вариант 14.
# Разработайте систему начисления очков для задачи 6, в соответствии с которой игрок получал бы большее количество баллов за меньшее количество попыток.

# Kolov A.A
# 25.05.2016

import random
attempt = 5
mascots = ['Леопард','Белый Мишка','Зайка']
progSel = mascots[random.randint(0,2)]
print("Компьютер загадал одного из талисманов Олимпиады в Сочи. Сможете ли вы его удадать? ")
while attempt > 0:
	userSel = input()
	if userSel==progSel:
		print("Верно! Это действительно " + userSel)
		break
	else:
		print("Неверно! Это не " + userSel + "! Попробуйте еще раз")
		attempt = attempt - 1
		print("У вас осталось " + str(attempt) + " попыток")
print("Игра окончена! Вы набрали " + str(10*attempt) + " баллов")	
input()