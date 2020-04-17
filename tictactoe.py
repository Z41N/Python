"""
-------------------------------------------------------------------------------
ZA1N's TIC-TAC-TOE (IN PROCESS AS OF 4/17/20)
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
    position = input("Enter a position from 1 to 9: ")
    position = int(position) - 1
    board[position] = "X"
    current_player = "X"
    display_board()


# Allowing player O to make turn
def handle_turn_o():
    global current_player
    position = input("Enter a position from 1 to 9: ")
    position = int(position) - 1
    board[position] = "O"
    current_player = "O"
    display_board()


# Checking for win
def win_checker():
    global is_game_on
    if board[0] == board[1] == board[2] != "-":
        print(board[0] + " won!")
        is_game_on = False


# Checking for tie
def tie_checker():
    pass


# Start the game using a method
def start_game():
    global is_game_on
    is_game_on = True
    display_board()
    while is_game_on:
        handle_turn_x()
        win_checker()
        tie_checker()
        handle_turn_o()


start_game()
