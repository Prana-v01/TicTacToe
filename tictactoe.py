import random

board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"] #this is the slots for the board.
print(len(board))

def bot_move(board):
    while True:
        bot_move = random.randint(0,8)
        if board[bot_move] == "-": #len(board)+1), same thing.
            board[bot_move] = "o"
        break

def bot_win():
    if board[0] == "o" and board[1] == "o" and board[2] == "o": #first row str8
        return True
    elif board[3] == "o" and board[4] == "o" and board[5] == "o":
        return True
    elif board[6] == "o" and board[7] == "o" and board[8] == "o":
        return True
    elif board[0] == "o" and board[4] == "o" and board[8] == "o": #diagnol left to right
        return True

def print_board(board): #using the board variable, we can create the lines that seperate x's and o's
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("-----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("-----------")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("-----------")

def player_choice(board):
    while True:
        player_choice = int(input("Select a spot 1-9: "))
        if player_choice in range(1,10) and board[player_choice-1] == "-": #len(board)+1), same thing.
            board[player_choice-1] = player_x_o
            break #i forgot to put this in and thats why it was not updating the board in real time.
        else:
            print("try again!")

player_x_o = input("choose 'x' or 'o': ") #validate

def player_win_condition(board,player_x_o):
    if board[0] == player_x_o and board[1] == player_x_o and board[2] == player_x_o: #first row str8
        return True
    elif board[3] == player_x_o and board[4] == player_x_o and board[5] == player_x_o:
        return True
    elif board[6] == player_x_o and board[7] == player_x_o and board[8] == player_x_o:
        return True
    elif board[0] == player_x_o and board[4] == player_x_o and board[8] == player_x_o: #diagnol left to right
        return True
    else:
        return False


while True:
    print_board(board)
    player_choice(board)
    if player_win_condition(board,player_x_o):
        print_board(board)
        print("you won!")
        break
    bot_move(board)
    print("bots move\n")
    if bot_win():
        print("bot won")
        print_board(board)
        break

"""
10:48pm 22/07/04
- clean it up (make the board more sexy)
- gamemodes
- add more win conditions
- levels? (normal, hard)
- simplify code 
- increase efficency
- 

"""