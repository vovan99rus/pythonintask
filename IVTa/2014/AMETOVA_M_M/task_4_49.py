# Задача 4. Вариант 49
# Напишите программу, которая выводит имя, под которым скрывается Саид-Мурадзола Садриддин. # Дополнительно необходимо вывести область интересов указанной личности, место рождения, годы # рождения и смерти (если человек умер), вычислить возраст на данный момент (или момент # смерти). Для хранения всех необходимых данных требуется использовать переменные. После вывода # информации программа должна дожидаться пока пользователь нажмет Enter для выхода.

# Ametova M. M.
# 31.03.2016


name = "Саид-Мурадзола Садриддин"
famousName = "Айни"
interests = ["писатель", "общественный деятель", "учёный"]
birthPlace = "Сактари"
day = 0
month = 1
year = 2
daysInYear = 365
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
birthday = [27, 4, 1878]
deathday = [15, 7, 1954]

def getAge(birthDate, deathDate):
    if birthDate[month] == deathDate[month]:
        if birthDate[day] >= deathDate[day]:
            return deathDate[year] - birthDate[year] - 1
    if birthDate[month] > deathDate[month]:
        return deathDate[year] - birthDate[year] - 1
    return deathDate[year] - birthDate[year]
    
def printDate(date):
    dateStr = ''
    if date[day] < 10:
        dateStr += '0'
    dateStr += str(date[day]) + '.'
    if date[month] < 10:
        dateStr += '0'
    dateStr += str(date[month]) + '.' + str(date[year])
    print(dateStr)

print(name, ", более известныый как ", famousName, sep = '', end = ".\n\n")
print ("Интересы\t:", end = ' ')
i = 0
for interest in interests:
    if (i < interests.__len__() - 1):
        print (interest, end = ", ")
        i += 1
    else:
        print (interest, end = ".\n")
print("Дата рождения\t:", end = ' ')
printDate(birthday)
print("Дата смерти\t:", end = ' ')
printDate(deathday)
print("Возраст на момент смерти:", getAge(birthday, deathday), "лет")
input("\nНажмите Enter для выхода.")