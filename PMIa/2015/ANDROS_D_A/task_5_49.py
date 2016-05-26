#Задача 5.Вариант 49.
#Напишите программу, которая бы при запуске случайным образом отображала название одного из девяти действующих вокзалов Москвы.
#Andros D.A.
#28.04.2016
import random
vokzaly=["Belorusskiy","Kazanskiy","Kievskiy","kurskiy","Leningradskiy","Paveletskiy","Riszkiy","Savelovskiy","Yaroslavskiy"]
v=random.choice(vokzaly)
print(v)
