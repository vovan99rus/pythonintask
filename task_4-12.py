# Задача 4. Вариант 12
#
#Напишите программу, которая выводит имя, под которым скрывается Лариса Петровна Косач-Квитка.
#Дополнительно необходимо вывести область интересов указанной личности, место рождения,
#годы рождения и смерти (если человек умер), вычислить возраст на данный момент (или момент смерти).
#Для хранения всех необходимых данных требуется использовать переменные.
#После вывода информации программа должна дожидаться пока пользователь нажмет Enter для выхода.

# Курятников П.В
# 25.05.2016 

a ="Larisa Petrovna Kosach-Kvitka, naibolee izvestna kak Lesya Ukrainka"
b ="Zhitomirakaya oblast, Ukraine"
born = 1871
died = 1913
life = died - born
interests ="Pisat poemi"
print(a)
print("Mesto rozhdeniya:", b)
print("Data rozhdenya:", born)
print("Data smerti:", died)
print("Ona prozhila",life,"goda")
print("Interesi:" , interests)
input("type 'enter'")

