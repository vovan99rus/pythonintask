# Задача 5. Вариант 15.
# Напишите программу, которая бы при запуске случайным образом отображала название одного из двенадцати городов, 
# входящих в Золотое кольцо России.

# Mitin D.S.
# 30.03.2016, 21:03.
import random
start = "Один из городов Золотого кольца является: "
choice = random.randint(1,12)
if choice == 1:
    print(start+"Переславль-Залесский")
elif choice == 2: 
    print(start+"Ростов Великий")
elif choice == 3: 
	print(start +"Углич")
elif choice == 4: 
	print(start +"Ярославль")
elif choice == 5: 
	print(start +"Кострома")
elif choice == 6: 
	print(start +"Плёс")
elif choice == 7: 
	print(start +"Суздаль")
elif choice == 8: 
	print(start +"Владимир")
elif choice == 9: 
	print(start +"Александров")
elif choice == 10: 
	print(start +"Сергиев Посад")
elif choice == 11: 
	print(start +"Тутаев")
elif choice == 12: 
	print(start +"Юрьев-Польский")
input("Нажмите ENTER для продолжения")
