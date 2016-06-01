#Задача 5. Вариант 21.
#Напишите программу, которая бы при запуске случайным образом отображала название одной из двадцати восьми стран, входящих в Европейский союз.

#Шпенькова А.С.
#11.04.2016
import random
n = random.randint (1,28)

if n==1:
	print ("Австрия")
elif n==2:
	print ("Бельгия")
elif n==3:
	print ("Болгария")
elif n==4:
	print ("Венгрия")
elif n==5:
	print ("Великобритания")
elif n==6:
	print ("Греция")
elif n==7:
	print ("Германия")
elif n==8:
	print ("Дания")
elif n==9:
	print ("Италия")
elif n==10:
	print ("Ирландия")
elif n==11:
	print ("Испания")
elif n==12:
	print ("Республика Кипр")
elif n==13:
	print ("Люксембург")
elif n==14:
	print ("Латвия")
elif n==15:
	print ("Литва")
elif n==16:
	print ("Мальта")
elif n==17:
	print ("Нидерланды")
elif n==18:
	print ("Португалия")
elif n==19:
	print ("Польша")
elif n==20:
	print ("Румыния")
elif n==21:
	print ("Словения")
elif n==22:
	print ("Словакия")
elif n==23:
	print ("Франция")
elif n==24:
	print ("Финляндия")
elif n==25:
	print ("Хорватия")
elif n==26:
	print ("Чехия")
elif n==27:
	print ("Швеция")
elif n==28:
	print ("Эстония")

input("\n\nНажмите Enter для выхода.")
