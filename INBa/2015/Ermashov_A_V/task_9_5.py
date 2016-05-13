import random
spisok=("александр", "программа", "клавиатура", "руки", "голова", "студент", "информатика")
zagadannoe=random.choice(spisok)
proverka=zagadannoe
kolvo=len(zagadannoe)
bykva = random.randrange(kolvo)
i=4
print("Поиграем в игру. Я загадываю слово, ты должен отгадать его. Но сначала ты можешь отгадать буквы в этом слове.\nУ тебя 5 попыток.")
print("Я загадал слово. Если я не ошибься, в нем",kolvo,"букв.")
poisk=input("Введи букву: ")
while i>0:
	if poisk in proverka:
		print("Есть такая буква")
	else: print("Нет такой буквы")
	i-=1
	poisk=input("Введи еще букву: ")
poisk=input("Попытки кончились, теперь отгадай слово: ")
while poisk != zagadannoe:
	poisk=input("Неправильно. Попробуй еще раз: ")
print("Ты прав! Это слово",zagadannoe,"!")
input("Нажми ENTER для продолжения")