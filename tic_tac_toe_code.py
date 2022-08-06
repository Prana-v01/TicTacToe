board = ['▢','▢','▢','▢','▢','▢','▢','▢','▢']

def print_board(): # board will be displayed
    print(board[0],board[1],board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])

print_board() #displaying board

def validate(board,player): #to validate the users input of position on board.
    while player not in range(1,10) or board[player-1] != '▢': #checks if player is not in valid range or if theres already slot being used. If either is True, contiue.
        player = int(input("Please enter a valid position: ")) # asks for new position, as the previous one was incorrect.
    return player-1 #It returns -1 so we recieve the index and is able to place in the correct place.

def win_conditions(player_value,player_name): #this will determnie who wins.
    win_conditions = [[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6],[0,3,6],[1,4,7],[2,5,8]] # the possible win combinations.
    for wins in win_conditions: #each list in the list of lists.
        occurence_of_combination = 0 #keeps track of how many time the occurence of a correct combination occures.
        for num in player_value: #the single element inside the original list of users input
            if num in wins: #checks if that single element is iniside of a list inside the list of lists.
                occurence_of_combination += 1 # if yes, it adds +1 
                if occurence_of_combination >= 3: # once the user has 3 correct occurences, it translates to a win. 
                    return True

#these are to store the input given by the two users.
p1_value = []
p2_value = []

#this is the game. (Could also make this a function).
while True:
    player_one = int(input("enter a number: "))
    player_one_valid = validate(board,player_one) #validates the users input, then stores, so we can further use.
    p1_value.append(player_one_valid) #the validated version of the users input will then be appended to p1_value.
    board[player_one_valid] = "x" # places "x" on the board of the desired place by the user.
    print_board() #displays board

    # checks if game is finished by determining the amount of slots. When no slots are availbile the game will end.
    # this is flawed in a way, this should end when somone wins. Or fill up the slots if its a tie. 
    if board[0] and board[1] and board[2] and board[3] and board[4] and board[5] and board[6] and board[7] and board[8] != "▢":
        break

    player_two = int(input("enter a number: "))
    player_two_valid = validate(board, player_two)
    p2_value.append(player_two_valid)
    board[player_two_valid] = "o"
    print_board()

if win_conditions(p1_value,"Player One"):
    print("Player one has won!") # display who wins.

if win_conditions(p2_value,"Player Two"):
    print("player two has won!")

