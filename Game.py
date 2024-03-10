# File: Game.py
# Purpose: Tic Tac Toe.
#          it's made to have a little fun with your friends
# Author: Marwan Hussein Galal
# version: 1.0
# Last Modification Date: 2-3-2024
#___________________________________________________________________________#
import time
# Functions
#----------------------#
# Rules
def game_rules():
    rules ="""
rules:
1- The game is played on a grid that's 3 squares by 3 squares.

2- You are X , your friend (or the computer in this case) is O . Players take turns putting their marks in empty squares.

3- The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.

4- When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.

=================================
|          |          |         |
|          |          |         |
|          |          |         |
|          |          |         |
|===============================|
|          |          |         |
|          |          |         |
|          |          |         |
|          |          |         |
|===============================|
|          |          |         |
|          |          |         |
|          |          |         |
|          |          |         |
=================================
how to play:
1- To beat the computer (or at least tie), you need to make use of a little bit of strategy.
Strategy means figuring out what you need to do to win.

2- Part of your strategy is trying to figure out how to get three X s in a row.
The other part is trying to figure out how to stop the computer from getting three O s in a row.

3- After you put an X in a square, you start looking ahead. Where's the best place for your next X ?
You look at the empty squares and decide which ones are good choices which ones might let you make three X s in a row.

4- You also have to watch where the computer puts its O . That could change what you do next. If the computer gets two O s in a row,
you have to put your next X in the last empty square in that row, or the computer will win. You are forced to play in a particular square or lose the game.

5- If you always pay attention and look ahead, you'll never lose a game of Tic-Tac-Toe. You may not win, but at least you'll tie.
"""
    print(rules)

# initialize board-----------------------------------------------
board = ['1','2','3',
        '4','5','6',
        '7','8','9']
def n_board(board):
    print(" ___________")
    print("|" ,board[0], "|" ,board[1], "|" ,board[2], "|")
    print("|-----------|")
    print("|" ,board[3], "|" ,board[4], "|" ,board[5], "|")
    print("|-----------|")
    print("|" ,board[6], "|" ,board[7], "|" ,board[8], "|")
    print("|___________|")

#winner-or-tie---------------------------------------------
def horizontal(board):# checks winner horizontally by checking each row
    global winner
    if board[0] == board[1] == board[2]:
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5]:
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8]:
        winner = board[6]
        return True

def vertical(board):# checks winner vertically by checking each coloumn
    global winner
    if board[0] == board[3] == board[6]:
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7]:
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8]:
        winner = board[2]
        return True

def cross(board):# checks winner of cross by checking each diagonal
    global winner
    if board[0] == board[4] == board[8]:
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6]:
        winner = board[1]
        return True
    
def tie(board):
    # Move through each possition on the board
    for space in board:
        # If the space is a digit, it's empty, so return False
        if space.isdigit():
            return False
    # If all spaces are filled with 'X' or 'O', return True indicating a tie
    return True

# Validates all the previous functions together
def maincheck(board, playermove):
    # Check for horizontal, vertical, or diagonal win
    if horizontal(board) or vertical(board) or cross(board):
        # Display the final board state
        n_board(board)
        # Print the winner
        print(f"\n***PLAYER of {playermove} is the winner***\n")
        return True
    # Check for a tie
    elif tie(board):
        # Display the final board state
        n_board(board)
        # Print that the game ended in a tie
        print("\n***It's a tie!***\n")
        return True
    # If neither win nor tie, return False to indicate the game continues
    return False
#------------------------------------------------------------
def playing_possetion(board,playermove):
    while True:
        play = int(input(f"\nPlayer of {playermove} please enter number from 1-9: "))
        # Check if the input is within the valid range and the selected position is empty
        if play >= 1 and play <= 9 and board[play - 1] not in ("X", "O"):
            # Update the board with the player's move
            board[play - 1] = playermove
            # Check if the game has ended after the player's move
            if maincheck(board, playermove):
                return 'END'# If the game has ended, return 'END' to signal the end of the game
            break# Break out of the loop to allow the next player to make a move
        else:
            # If the input is invalid (position already taken or out of range), prompt the player to enter a valid move
            print("Please enter a valid move")

def game():
    print("\nWELCOME TO TIC TAC TOE\n")
    # allows both players to make moves
    while True:
        n_board(board)
        if playing_possetion(board,"X") == 'END': # Player1
            break
        else:
            n_board(board)
            if playing_possetion(board,"O") == 'END': # Player2
                break

def main():
    main_menu ="""
                |**Main Menu**|
    ---------------------------------------
    A) Game Rules
    B) Play
    C) Exit
    """
    while True:
        print(main_menu)
        choice = input("Enter your choice: ").upper()
        if choice == "A":
            game_rules()
        elif choice == "B":
            game()
            print ("Good Bye\n")
            time.sleep(2)
            break
        elif choice == "C":
            print ("\n******** Good Bye ********\n")
            break
        else:
            print ("Please enter a valid choice")
#=========================================================================#
# Program
main()