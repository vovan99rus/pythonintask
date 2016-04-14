# Задача 8. Вариант 23
# Доработайте игру "Анаграммы" (см. М.Доусон Программируем на Python. Гл.4)
# так, чтобы к каждому слову полагалась подсказка. Игрок должен получать право
# на подсказку в том случае, если у него нет никаких предположений.
# Разработайте систему начисления очков, по которой бы игроки, отгадавшие
# слово без подсказки, получали больше тех, кто запросил подсказку.

# Moshkov Y. O.
# 14.04.2016

import random
words = ("python", "shell", "interpreter", 
"log", "java", "style", "float")
word = random.choice(words)
print("Игра \"Анаграммы\"")
anagram = ""
correct = word
while word:
        pos = random.randrange(len(word))
        anagram += word[pos]
        word = word[:pos] + word[pos + 1:]
print("Ваша анаграмма:", anagram)
answer = input("Введите ваш ответ: ")
while answer != correct:
        answer = input("Неправильный ответ. Попробуйте ещё раз: ")

input("Вы выиграли! \nНажмите Enter для выхода")
