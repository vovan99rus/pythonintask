# Задача 10. Вариант 14.
# Напишите программу "Генератор персонажей" для игры. Пользователю должно быть предоставлено 30 пунктов, которые можно распределить между четырьмя характеристиками:
# Сила, Здоровье, Мудрость и Ловкость. Надо сделать так, чтобы пользователь мог не только брать эти пункты из общего "пула", но и возвращать их туда из характеристик, которым он решил присвоить другие значения

# Kolov A.A
# 27.05.2016

pool = 30
character = []
print("Введите 1,чтобы начать ")
while 0==0:
	choose = input()
	#Очищяем пул и характеристики в случае, если пользователь после решает изменить характерстики
	if (str(choose)) == "2":
		pool = 30
		character.clear()
	#Задаём характеристики(имя задаётся только, если пользователь ввёл 1, т.е. создаёт нового персонажа)
	if (str(choose)) == "1" or (str(choose)) == "2":
		if (str(choose) == "1" ):
			name = input("Введите имя персонажа ")
		print("Остаток поинтов " + str(pool))
		force = int(input("Введите силу значением от 1 до " + str(pool-3)+" "))
		if (force>=1 and force<=pool-3):
			character.insert(0,force)
			pool = pool - force
		else:
			print("Неверные значения")
			while force < 1 or force > pool-3:
				force = int(input("Введите силу значением от 1 до " + str(pool-3)+" "))
				if (force > 1 and force < pool-3):
					character.insert(0, force)
					pool = pool - force
					break
		print("Остаток поинтов " + str(pool))
		health = int(input("Введите здоровье значением от 1 до " + str(pool-2)+" "))
		if (health >= 1 and health <= pool-2):
			character.insert(1, health)
			pool = pool - health
		else:
			print("Неверные значения")
			while health < 1 or health > pool - 2:
				health = int(input("Введите здоровье значением от 1 до " + str(pool - 2) + " "))
				if (health > 1 and health < (pool - 2)):
					character.insert(1, health)
					pool = pool - health
					break


		print("Остаток поинтов " + str(pool))
		mind = int(input("Введите мудрость значением от 1 до " + str(pool-1)+" "))
		if (mind >= 1 and mind <= pool - 1):
			character.insert(2, mind)
			pool = pool - mind
		else:
			print("Неверные значения")
			while mind < 1 or mind > pool - 1:
				mind = int(input("Введите мудрость значением от 1 до " + str(pool - 1) + " "))
				if (mind > 1 and mind < (pool - 1)):
					character.insert(2, mind)
					pool = pool - mind
					break


		print("Остаток поинтов " + str(pool))
		dexterity = int(input("Введите ловкость значением от 1 до " + str(pool) + " "))
		if (dexterity >= 1 and dexterity <= pool):
			character.insert(2, dexterity)
			pool = pool - dexterity
		else:
			print("Неверные значения")
			while dexterity < 1 or dexterity > pool:
				dexterity = int(input("Введите ловкость значением от 1 до " + str(pool) + " "))
				if (dexterity > 1 and dexterity < (pool)):
					character.insert(2, dexterity)
					pool = pool - dexterity
					break
		print("Остаток поинтов " + str(pool))
		print("Введите 1, чтобы создать персонажа заново. Введите 2, чтобы изменить его характеристики. Введите 'Создать', чтобы закончить")

	elif (choose == "Создать"):
		print("""Ваш персонаж с именем """ + name + """ создан! Его характеристики:
			Сила: """ + str(force) + """
			Здоровье: """ + str(health) + """
			Мудрость: """ + str(mind) + """
			Ловкость: """ + str(dexterity))
input()