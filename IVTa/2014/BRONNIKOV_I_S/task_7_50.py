Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Задача 7. Вариант 50
# Создайте игру, в которой компьютер загадывает нназвание одной из пятнадцати республик,
# входящих в состав СССР, а игрок должен его угадать.

# Bronnikov I. S.
# 25.05.2016

import random
USSR = ["РСФСР", "Украинская ССР", "Белорусская ССР" "Узбекская ССР" "Казахская ССР" "Грузинская ССР" "Азербайджанская ССР" "Литовская ССР" "Молдавская ССР" "Латвийская ССР" "Киргизская ССР" "Таджикская ССР" "Армянская ССР" "Туркменская ССР" "Эстонская ССР"]
number = random.randint(0, 14)
Republics = USSR[number].lower()

inputRepublics = input("Угадайте одну из 15 республик СССР: ")
score = 14
while inputRepublics != republics :
        inputRepublics = input("Вы не угадали, попробуйте ещё раз: ")
        if (score > 0):
                score -= 1
out = "Вы угадали! Ваш счёт " + str(score) + ". Нажмите Enter для выхода."
input(out)
