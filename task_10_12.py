# Задача 10. Вариант 12
#
##1-50. Напишите программу "Генератор персонажей" для игры. Пользователю должно быть предоставлено 30 пунктов, которые можно распределить между четырьмя характеристиками: Сила, Здоровье, Мудрость и Ловкость. Надо сделать так,
#чтобы пользователь мог не только брать эти пункты из общего "пула", но и возвращать их туда из характеристик, которым он решил присвоить другие значени
# Курятников П.В
# 25.05.2016 



punkti = 30
ochki = 30
geroy ={"Сила" : "0", "Здоровье" : "0", "Мудрость": "0", "Ловкость": "0" }
menu = None
punktiki= 0

while choise !=4: 
    print ("1 - Добавить очки к характеристике, 2- уменьшить очки к характеристике, 3 - просмотр характеристик, 4 -выход ")
    menu = input ("Выбор пункта меню:")
    if menu == 1:
        print("Пожалуйста, введите характеристику", len(person), "характеристики:")
        for item in person:
            print(item)
        haract= str(input("\n:"))
        haract = haract.title()
        while haract not in geroy:
            print("Данной характеристики не существует")
            haract = str(input("\n"))
            char = char.title()
        else:
            print("Введите количество очков. Вы имеете", ochki, "неиспользованных очков")
            punktiki  = int(input("\n:"))
        geroy[haract] = punktiki
        print (punktiki, "очков было добавено к ", haract)
        ochki -= punktiki
    elif menu == 2:
        print ("\nДоступно", len(geroy), "характеристики для уменьшения пунктов:")
        for item in geroy:
            print(item)
        haract =str(input("ведите характеристику:"))
        haract = haract.title()
        while haract not in geroy:
            haract = str(input("Данной характеристики не существует"))
            haract = haract.title()
        else:
            print("Доступно", geroy, "пунктов.")
            punktiki = int(input("Подтвердите  удаление:")
        geroy[haract] = punktiki
        print(punktiki, "очков успешно удалено.")
        ochki +=punkti
    elif menu == 3:
        print("\nХарактеристики вашего героя")
        for item in geroy:
            print(item, "\t\t" geroy [item])
    elif menu ==4:
        print ("Выход")

input ("\nНажмите Enter для выхода.")

    
            
            
        
