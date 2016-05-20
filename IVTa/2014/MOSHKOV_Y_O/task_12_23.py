# Задача 12. Вариант 23
# Разработайте игру "Крестики-нолики".
#(см. М.Доусон Программируем на Python гл. 6).

# Moshkov Y. O.
# 20.05.2016

from tkinter import *

class Game:
    crturn = True
    field = []
    def __init__(self):
        for i in range (3):
            self.field.append(['', '', ''])
    def move(self, pos):
        self.fill_pos(pos)
        if self.checkWin():
            winner = "Нолики"
            if self.crturn:
                winner = "Крестики"
            if (messagebox.askquestion("Победа!", winner +
                                       " выиграли. Начать заново?")) == "yes":
                newGame(buttons)
                self.clear()
            else:
                gui.destroy()
        self.crturn = not self.crturn
    def fill_pos(self, pos):
        if self.crturn:
            self.field[int(pos / 3)][pos % 3] = 'X'
        else:
            self.field[int(pos / 3)][pos % 3] = 'O'
        for elem in self.field:
            print(elem)
    def checkWin(self):
        print("Checking...")
        if self.crturn:
            unit = 'X'
        else:
            unit = 'O'
        # Rows
        for row in self.field:
            win = True
            for i in row:
                if i != unit:
                    win = False
            if win == True:
                return True
        # Columns
        for col in range (3):
            win = True
            for row in range (3):
                if self.field[row][col] != unit:
                    win = False
            if win == True:
                return True
        # Diagonals
        for i in range (0, 3, 2):
            win = True
            for j in range (3):
                if self.field[i + j * (i * -1 + 1)][j] != unit:
                    win = False
            if win == True:
                return True
    def clear(self):
        for i in range (3):
            for j in range (3):
                self.field[i][j] = ''
                

game = Game()

# GUI

def act(num, game, button):
    if (game.crturn):
        button["text"] = 'X'
    else:
        button["text"] = 'O'
    game.move(num)

def newGame(buttons):
    for btn in buttons:
        btn["text"] = ''

gui = Tk()
buttons = []
for i in range (9):
    buttons.append(Button(gui, text = "", font = "arial, 48", width = 3,
                          command = lambda i = i: act(i, game, buttons[i])))
    buttons[i].grid(row = int(i / 3), column = i % 3)
gui.mainloop()
