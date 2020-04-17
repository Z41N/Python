"""
-------------------------------------------------------------------------------
ZA1N's TIC-TAC-TOE
1.) Create the board
2.) Display the board
3.) Handle turn
4.) Check if win (row, column, across)
5.) Check if tie
6.) Flip player
-------------------------------------------------------------------------------
"""

# Global Variables
is_game_on = ""
current_player = ""

# Creating the board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


# Displaying the board using a method
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# Allowing player X to make turn
def handle_turn_x():
    global current_player
    position = input("Enter a position from 1 to 9:")
    position = int(position) - 1
    board[position] = "X"
    current_player = "X"
    display_board()


# Allowing player O to make turn
def handle_turn_o():
    global current_player
    position = input("Enter a position from 1 to 9:")
    position = int(position) - 1
    board[position] = "O"
    current_player = "O"
    display_board()


# Checking for win using row and column checkers
def win_checker():
    if row_win_checker():
        return True
    elif col_win_checker():
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


# Checking for tie
def tie_checker():
    pass


# Start the game using a method
def start_game():
    global is_game_on
    is_game_on = True
    print("\n")
    print("-----------")
    print("TIC-TAC-TOE")
    print("-----------\n")
    display_board()
    while is_game_on:
        handle_turn_x()
        if win_checker():
            break
        tie_checker()
        handle_turn_o()
        if win_checker():
            break


start_game()
