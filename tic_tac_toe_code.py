board = ['▢','▢','▢','▢','▢','▢','▢','▢','▢']

def print_board():
    print(board[0],board[1],board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])

print_board()

def validate(board,player): #validates user's choice
    while player not in range(1,10) or board[player-1] != '▢': #loop will only be triggered if user's responce is invalid.
        player = int(input("Please enter a valid position: ")) #asks for new number
    return player-1 #returns the correct number.

def game_conditions(board): #win conditions -> not finished. Implementing: Tie, Player 2's win (else)
    if board[0] == "x" and board[1] == "x" and board[2] == "x":
        print("player 1 won!")
    elif board[3] == "x" and board[4] == "x" and board[5] == "x":
        print("player 1 has won!!")
    elif board[6] == "x" and board[7] == "x" and board[8] == "x":
        print("player 1 has won")
        ### horizonal player 1 win
    elif board[0] == "x" and board[4] == "x" and board[8] == "x":
        print("player 1 has won")
    elif board[2] == "x" and board[4] == "x" and board[6] == "x":
        print("player 1 has won!")
        ### Diagnoal player 1 win
    elif board[0] == "x" and board[3] == "x" and board[6] == "x":
        print("player 1 has won")
    elif board[1] == "x" and board[4] == "x" and board[7] == "x":
        print("player 1 has won")
    elif board[2] == "x" and board[5] == "x" and board[8] == "x":
        print("player 1 has won")
        ### vertical player 1
    else:
        print("player two won!")
        # if none of them are True, player 2 must have won. Or a tie...

while True: #this is the gameplay
    player_one = int(input("enter a number: "))
    player_one_valid = validate(board,player_one) #calls validate and stores it in player_one_valid, because its the valid responce hence valid.
    board[player_one_valid] = "x" #sets "x" in that position the user desired-1 
    print_board()

    if board[0] and board[1] and board[2] and board[3] and board[4] and board[5] and board[6] and board[7] and board[8] != "▢":
        break #checks if the board is full.
        #i wouldnt need this if i complete the conditions and i can also implement the gameplay as a function.

    player_two = int(input("enter a number: "))
    player_two_valid = validate(board, player_two)
    board[player_two_valid] = "o"
    print_board()



print()
game_conditions(board) #determines who won.




