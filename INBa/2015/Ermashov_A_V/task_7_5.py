import random
schet=10000
cvet = random.randint(1,3)
if cvet == 1: cvet="Красный"
elif cvet ==2: cvet="Желтый"
elif cvet ==3: cvet="Зеленый"
print("Угадайте цвет светофора. ")
otvet = input("\nВведите цвет: ")
while(otvet != cvet):
    print("\nНеправильно. Попробуй еще раз")
    otvet = input("\nВведите цвет: ")
    schet-=1500
    if schet<=0: 
    	break
if schet>0:
	print("Правильно! Это", cvet,"цвет!")
	print("Вы набрали",schet," очков! Поздравляем!")
else: print("К сожалению, вы проиграли. У вас 0 очков. Загаданный цвет:",cvet)
input("Нажмите ENTER для продолжения")