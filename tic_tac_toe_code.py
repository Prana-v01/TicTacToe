board = ['▢', '▢', '▢', '▢', '▢', '▢', '▢', '▢', '▢']  # the format of the board.
empty_slot = '▢'

def print_board():  # board will be displayed
    """
    Purpose: This prints a nice version of the board, in the traditional way tic tac toe is played.
    Parameters: None
    Return: print
    """
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])

print_board()  # displaying board

def validate(board, player):  # to validate the users input of position on board.
    """
    Purpose: This function validates the users input. It takes in the orginal value and checks to see if it meets the critera set.
    If the criteria is not met for any reason, it will give them an option to try another input.
    Parameters:
    1) board: The board is here so we can check one of the conditions, if the specific slot if allready being used.
    2) player: This is to recieve the users input.
    Return: player-1, which gives the index and is usable in relation to the board.
    """
    while player not in range(1, 10) or board[
        player - 1] != empty_slot:  # checks if player is not in valid range or if theres already slot being used. If either is True, contiue.
        player = int(
            input("Please enter a valid position: "))  # asks for new position, as the previous one was incorrect.
    return player - 1  # It returns -1 so we recieve the index and is able to place in the correct place.

def win_conditions(player_value):  # this will determnie who wins.
    """
    Purpose: This function determines who wins the match
    Parameters:
    1) player_value: This takes in the player's value (their valid inputs) and try to match them with one of the winning combinations)
    Return: True
    """
    win_conditions = [[0, 1, 2], [3, 4, 5],
                      [6, 7, 8], [0, 4, 8],
                      [2, 4, 6], [0, 3, 6],
                      [1, 4, 7],[2, 5, 8]]  # the possible win combinations.
    for wins in win_conditions:  # each list in the list of lists.
        occurence_of_combination = 0  # keeps track of how many time the occurence of a correct combination occures.
        for num in player_value:  # the single element inside the original list of users input
            if num in wins:  # checks if that single element is iniside of a list inside the list of lists.
                occurence_of_combination += 1  # if yes, it adds +1
                if occurence_of_combination >= 3:  # once the user has 3 correct occurences, it translates to a win.
                    return True

# these are to store the input given by the two users.
p1_value = []
p2_value = []

def winner(p1_value,p2_value):
    """
    :param p1_value: values of the player one
    :param p2_value: values of the player two
    :return: exit()
    """
    if win_conditions(p1_value):
        print("player 1 won")
        exit()
    elif win_conditions(p2_value):
        print("player 2 won!")
        exit()

# this is the game. (Could also make this a function).
def board_change_move():
    pass

while True:
    player_one = int(input("enter a number: "))
    player_one_valid = validate(board, player_one)  # validates the users input, then stores, so we can further use.
    p1_value.append(player_one_valid)  # the validated version of the users input will then be appended to p1_value.
    board[player_one_valid] = "x"  # places "x" on the board of the desired place by the user.
    print_board()  # displays board

    winner(p1_value,p2_value)

    # checks if game is finished by determining the amount of slots. When no slots are availbile the game will end.
    # this is flawed in a way, this should end when somone wins. Or fill up the slots if its a tie.
    if empty_slot not in board:
        break  # when game is completely full.

    player_two = int(input("enter a number: "))
    player_two_valid = validate(board, player_two)
    board[player_two_valid] = "o"
    p2_value.append(player_two_valid)
    print_board()

print("Tie") #This occurs when the function winners, doesnt determine any of them to have won.
