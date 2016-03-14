import random
print('Задача 5')
Strana1=('Германия')
Strana2=('Италия')
Strana3=('Австро-Венгрия')
country=random.randint(1,3)
if country==1:
  print (Strana1)
if country==2:
	print(Strana2)
elif country==3:
	print(Strana3)

input('Нажмите Enter для выхода')