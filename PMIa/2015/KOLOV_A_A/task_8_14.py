# Задача 8. Вариант 14.
# Доработайте игру "Анаграммы" (см. М.Доусон Программируем на Python. Гл.4) так, чтобы к каждому слову полагалась подсказка. Игрок должен получать право на подсказку в том случае, если у него нет никаких предположений.
# Разработайте систему начисления очков, по которой бы игроки, отгадавшие слово без подсказки, получали больше тех, кто запросил подсказку.

# Kolov A.A
# 25.05.2016

import random

# create a sequence of words to choose from
WORDS = ("Питон", "Программирование", "Инкапсуляция", "Зачёт", "Сессия", "Сгущёнка")

hints = ("Язык программирования, на котором написана эта программа","процесс создания компьютерных программ","Один из 'столпов' ООП", "Чего хотят получить все студенты?","Чего бояться все студенты?","Вкусное, сладкое, из молока делается")
# pick one word randomly from the sequence
word = random.choice(WORDS)
wordNumber = WORDS.index(word)
# create a variable to use later to see if the guess is correct
correct = word
wantHint = "Подсказка"
countHints = 0
countErrors = 0
# create a jumbled version of the word
jumble =""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# start the game
print(
"""
           Welcome to Word Jumble!
        
   Unscramble the letters to make a word.
(Press the enter key at the prompt to quit.)
"""
)
print("The jumble is:", jumble + " Если вы сомневаетесь, введите 'Подсказка' ")

guess = input("\nYour guess: ")
while guess != correct and guess != "":
	if guess==wantHint:
		print(hints[wordNumber])
		countHints +=1
	if  guess!=wantHint:
		print("Sorry, that's not it.")
		countErrors +=1
		print("Число ошибок: " +str(countErrors))
	guess = input("Your guess: ")
	
		
if guess == correct:
		print("That's it!  You guessed it!\n")
	
	

print("Thanks for playing.")
print("Вы допустили " + str(countErrors) + " ошибок, использовали " + str(countHints) + " подсказок и заработали " + str(100-5*countErrors-50*countHints) + " очков")

input("\n\nPress the enter key to exit.")

