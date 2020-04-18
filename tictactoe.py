"""
-------------------------------------------------------------------------------
ZA1N's TIC-TAC-TOE

Remaining issues to fix (as of 4/18/20):
-------------------------------------------------------------------------------
"""

# Global Variables
is_game_on = ""
current_player = ""
position = ""

# Creating the board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


# Displaying the board using a method
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# Grab the user's choice and check integer (REPLACED WITH DOUBLE WHILE LOOP IN PLAYER METHODS)

# def input_number(message):
#     while True:
#         try:
#             position = int(input(message))
#         except ValueError:
#             print("\nNot a valid number. Please try again...\n")
#             continue
#         else:
#             return position - 1
#             break


# Allowing player X to make turn
def handle_turn_x():
    current_player = "X"
    print(current_player + "'s turn.")
    invalid = True
    position = input("Choose a number between 1 and 9: ")
    while invalid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a valid number: ")
        position = int(position) - 1
        if board[position] == "-":
            invalid = False
        else:
            print("You can't go there...Try again: ")
    board[position] = current_player
    display_board()
    print("\n")


# Allowing player O to make turn
def handle_turn_o():
    current_player = "O"
    print(current_player + "'s turn.")
    invalid = True
    position = input("Choose a number between 1 and 9: ")
    while invalid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a valid number: ")
        position = int(position) - 1
        if board[position] == "-":
            invalid = False
        else:
            print("You can't go there...Try again: ")
    board[position] = current_player
    display_board()
    print("\n")


# Checking for win using row and column checkers
def win_checker():
    if row_win_checker():
        return True
    elif col_win_checker():
        return True
    elif diag_win_checker():
        return True
    else:
        return False


# Checking if any rows are winners
def row_win_checker():
    if board[0] == board[1] == board[2] != "-":
        print("------")
        print(board[0] + " won!")
        print("------")
        return True
    elif board[3] == board[4] == board[5] != "-":
        print("------")
        print(board[3] + " won!")
        print("------")
        return True
    elif board[6] == board[7] == board[8] != "-":
        print("------")
        print(board[6] + " won!")
        print("------")
        return True
    else:
        return False


# Checking if any columns are winners
def col_win_checker():
    if board[0] == board[3] == board[6] != "-":
        print("------")
        print(board[0] + " won!")
        print("------")
        return True
    elif board[1] == board[4] == board[7] != "-":
        print("------")
        print(board[1] + " won!")
        print("------")
        return True
    elif board[2] == board[5] == board[8] != "-":
        print("------")
        print(board[2] + " won!")
        print("------")
        return True
    else:
        return False


# Checking if any diagnal wins
def diag_win_checker():
    if board[0] == board[4] == board[8] != "-":
        print("------")
        print(board[0] + " won!")
        print("------")
        return True
    elif board[2] == board[4] == board[6] != "-":
        print("------")
        print(board[2] + " won!")
        print("------")
        return True
    else:
        return False


# Checking for tie
def tie_checker():
    if "-" in board:
        return False
    else:
        print("-----")
        print("TIE!!")
        print("-----")
        return True


# Start the game using a method
def start_game():
    global board
    global is_game_on
    is_game_on = True
    print("\n")
    print("---------------")
    print("|             |")
    print("| TIC-TAC-TOE |")
    print("|             |")
    print("---------------\n")
    display_board()
    while is_game_on:
        handle_turn_x()
        if win_checker():
            break
        if tie_checker():
            break
        handle_turn_o()
        if win_checker():
            break
        if tie_checker():
            break
    # Attempt at restarting game if player wants to
    play_again = input("Do you want to play again? (Y/N) ")
    if play_again == 'y' or play_again == 'Y':
        board = ["-", "-", "-",
                 "-", "-", "-",
                 "-", "-", "-"]
        start_game()
    else:
        print("Exiting. Come back again soon!")
        exit()


start_game()
