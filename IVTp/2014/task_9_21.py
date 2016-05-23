#Задача 9. Вариант 21.
#Создайте игру, в которой компьютер выбирает какое-либо слово, а игрок должен его отгадать. 
#Компьютер сообщает игроку, сколько букв в слове, и дает пять попыток узнать, есть ли какая-либо буква в слове, причем программа может отвечать только "Да" и "Нет". 
#Вслед за тем игрок должен попробовать отгадать слово.

#Шпенькова А.С.
#23.05.2016

import random
 
 
 
word = ("зебра","слон","кот","носорог","динозавр","комар")
 
variant=""
 
computer_selection=random.choice (word)
 
tr1=5
x=1
i=1
 
print("\n Угадайте заданное слово...\n")
print ("\n",word, "\n")
print(computer_selection,"\n")
 
 
while variant!= computer_selection:
 
     
    if tr1==5 :
        
        
        if (input("нужны ли Вам подсказки?\n")) == "да" :
            print("Длина заданного слова = :",len(computer_selection),"\n")
        tr1=tr1-1
        
    if tr1 <= 0 :
        pass
    else :
        if tr1 <5 and tr1 >0 and x==0:
            if (input("нужна ли Вам ещё подсказка?\n")) == "да" :
                
                letter=input("Назовите букву и я скажу - есть ли она в слове :  ")
                if letter in computer_selection :
                    print("\n Эта буква присутствует в слове")
                else :
                    print ("буква отсутвует \n")
 
 
 
    variant=input("\n Ваш вариант :")
 
    
    if variant==computer_selection :
        print("Вы угадали!")
    else :
        "Вы ошиблись\n"
 

        
input("\n\nНажмите Enter, чтобы выйти...")