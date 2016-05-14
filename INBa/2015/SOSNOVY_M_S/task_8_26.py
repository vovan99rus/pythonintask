import random
ocki = 10
slova = ("хочу", "автомат", "программирование", "пожалуйста")
slovo = random.choice(slova)
bykv = len(slovo)
print ("Я загадал некоторое слово. В нем ", bykv, " букв." )
ls = list(slovo)
random.shuffle(ls)
anagramma = ls
i = 0
print(anagramma)
otv = ""
while(otv!=slovo):
	print("Вы готовы ввести слово?(да/нет)")
	otv = str(input())
	if (otv == str("да")):
		print("ВВодите свой ответ : ")
		otv = str(input())
		if (otv == slovo):
			if (ocki<0):
				ocki==0
			print("Поздравляю, Вы победили. Ваш счет: ", str(ocki))
	else:
		print("Хотите взять подсказку(да/нет)")
		otv = str(input())
		if (otv == str("да")):
			print("Подсказка!",i+1,"буква: ",slovo[i],"!")
			ocki-=1
		else:
			print("Вы не взяли подсказку и не ввели слово ==> вы сдались n/ GAME OVER")

input ("Нажмите ENTER для продолжения")