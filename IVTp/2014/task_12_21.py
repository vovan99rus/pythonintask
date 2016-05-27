# Задача 12. Вариант 21.
# Разработайте игру "Крестики-нолики".

# Шпенькова А.С.
# 27.05.2016

print("""
Добро пожаловать на игру крестики нолики 
чтобы сделать ход введите число от 0 до 8
	 
	          0 | 1 | 2
	          ---------
	          3 | 4 | 5
	          ---------
	          6 | 7 | 8""")
board=["-","-","-","-","-","-","-","-","-"]
bol=True
wins=False
schet=0
def disp(board):
     print("\n\t"+board[0]+" | "+board[1]+" | "+board[2]+"\n\t---------"+
	 "\n\t"+board[3]+" | "+board[4]+" | "+board[5]+"\n\t---------"+
	 "\n\t"+board[6]+" | "+board[7]+" | "+board[8]+"\n\t---------")
def win(board):
     twin=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
     for row in twin:
	     if board[row[0]]==board[row[1]]==board[row[2]]!="-":
		     return True
while wins!=True:
     if(schet==5):
         break
     if(bol):
         n1=input("\nХод игрока 1: ")
         if(board[int(n1)]=="-"):
             board[int(n1)]="X"
             disp(board)
             bol=False
             wins=win(board)
             schet+=1
         else:
	         print("Занято")
     else:
         n2=input("\nХод игрока 2: ")
         if(board[int(n2)]=="-"):
             board[int(n2)]="O"
             disp(board)
             bol=True
             wins=win(board)
         else:
	         print("Занято")
if(wins and bol):
     print("Победил игрок 2")
elif(wins and not bol):
     print("Победил игрок 1")
else:
     print("Ничья")
input('Нажмите Enter для выхода')