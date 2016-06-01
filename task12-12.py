# Задача 1. Вариант 12

# Разработайте игру "Крестики-нолики". (см. М.Доусон Программируем на Python гл. 6).

# Курятников П.В.
# 27.05.2016
player_name = input("Введите ваше имя:\n") 
def display_instruct():
       print(''' Добрый день, уважаемые зрители! Сегодня я, ваш незабываемый, сэр Эпофей,
    буду комментировать величайший гладиаторский интеллектуальный турнир, где сойдутся
    человек и компьютер.

    Добро пожаловать на игру "Крестики-Нолики"!

    В этот незабываемый матч мы узнаем, чьи мозги, крепки как орех, а чьи - разобьются в щепки, как деревяшка от топора!

    Также, сегодня мы узнаем, станет ли свободен наш участник или он отправится ... я уже слышу их рычание... отправится к очень... очень голодным тиграм! 

    Итак, мы начинаем!
    Объясняю правила нашей битвы:
    Чтобы сделать ход, нужно ввести число от 0 до 8, Числа соответствуют полям, как показано ниже

      0 | 1 | 2
      ---------
      3 | 4 | 5
      ---------
      6 | 7 | 8


       ''')


X = "Х" 
O= "О" 
EMPTY = " "
TIE= "Ничья" 
NUM_SQUARES = 9

def ask_yes_no(question):
    response=None
    while response not in ("y","n"):
        response=input(question).lower()
    return response
def pieces():
    go_first=ask_yes_no("Уважаемый",player_name, "хотите начать первым? (y/n): ")
    if go_first=="y":
        print("\n Итак, первый начинает играть ",player_name, ". Он играет крестиками.")
        human=X
        computer=O
    else:
        print("\n Игрок" ,player_name, "отказывается от первого хода, начинает компьютер. Человек будет играть за нолики.")
        computer=X
        human=O
    return computer, human
def new_board():
    board=[]
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8])

def legal_moves(board):
    moves = []
    for square in range(NUM_SQUARES):
        if board[square]== EMPTY:
            moves.append(square)
    return moves

def winner(board):
    WAYS_TO_WIN=((0, 1, 2),
		 (3, 4, 5),
		 (6, 7, 8),
		 (0, 3, 6),
		 (1, 4, 7),
		 (2, 5, 8),
		 (0, 4, 8),
		 (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]]==board[row[1]]==board[row[2]]!=EMPTY:
            winner=board[row[0]]
            return winner
        if EMPTY not in board:
            return TIE
    return None
def human_move(board, human):
    legal=legal_moves(board)
    move=None
    while move not in legal:
        move=ask_number("Наступил ход нашего героя.",player_name,", выберите одно из полей (0-8):", 0, NUM_SQUARES)
        if move not in legal:
            print("\n Увы! Это поле уже занято. Выберите другое.\n")
    print("Хорошо...")
    return move

def computer_move(board, computer, human):
    board=board[:]
    BEST_MOVES=(4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("Я выберу поле номер", end=" ")
    for move in legal_moves(board):
        board[move]=computer
        if winner(board)==computer:
            print(move)
            return move
        board[move] = EMPTY
    for move in legal_moves(board):
        board[move]=human
        if winner(board)==human:
            print(move)
            return move
            board[move]=EMPTY
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move
def next_turn(turn):
    if turn==X:
        return O
    else:
        return X
def congrat_winner(the_winner, computer, human):
    if the_winner !=TIE:
        print("Три", the_winner, "в ряд!\n")
    else:
        print("Ничья!\n")
    if the_winner==computer:
        print("Итак, побеждает... компьютер! Вот еще один довод в пользу того. что компьютеры превосходят людей решительно во всем! Голодные тигры благодарят вас за проигрыш!")
    elif the_winner==human:
        print("И так. фанфары... победитель - наш учеастник. Держите свой приз! Отныне и навсегда  вы свободный человек! А теперь отправляйтесь на все 4 стороны, пока я не предумал!" )
    elif the_winner==TIE:
        print("На поле ничья... А это значит, что завтра вы снова увидите нашего героя на нашем турнире!")
def main():
    display_instruct()
    computer, human=pieces()
    turn=X
    board=new_board()
    display_board(board)
    while  not winner(board):
        if turn==human:
            move=human_move(board, human)
            board[move]=human
        else:
            move=computer_move(board, computer, human)
            board[move]=computer
        display_board(board)
        turn=next_turn(turn)
    the_winner=winner(board)
    congrat_winner(the_winner, computer, human)
main()
input("\n\nНажмите Enter, чтобы выйти.")
