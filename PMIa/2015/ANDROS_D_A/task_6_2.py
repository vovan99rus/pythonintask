#Задача 6.Вариант 2.
#Создайте игру, в которой компьютер загадывает название одного из двенадцати созвездий, входящих в зодиакальный круг, а игрок должен его угадать.
#Andros D.A.
#28.04.2016
import random
sozvezdia=["Oven","Telec","Bliznetsy","Rak","Lev","Deva","Vesy","Skorpion","Strelec","Kozerog","Vodoley","Riby"]
s=random.choice(sozvezdia)
a=input("Введите 1 из созвездий")
if a==s:
   print("exactly")
else:
   print("you wrong")