#Задача №7 Вариант 9
#Программа пишет игру, в которой компьютер загадывает имя одного из трех поросят, а игрок должен его угадать и показывает кол-во баллов.


#Гасанов АФ
#28.03.2016
import random
porosyata=('Ниф-Ниф', 'Наф-Наф', 'Нуф-Нуф')
poros=random.randint(0,2)
Ball=100
rand=porosyata[poros]
print('Я загадал имя одного из трех поросят')
print (rand)
otvet=0

while (otvet)!=(rand):
	otvet=input('Введите имя одного из трех поросят:')
	if (otvet)!=(rand):
		print('Вы не угадали,попробуйте снова.')
		Ball-=15
	elif (otvet)==(rand):
		print('Вы угадали.')
		print('Ваши баллы:'+str(Ball))
		break
input('Нажмите Enter для выхода.')
