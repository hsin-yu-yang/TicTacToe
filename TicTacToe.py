'''
Solo Checkpoint 02
Author: Ella Yang
'''
# import os
# os.system("clear")

from IPython.display import clear_output
def main():
    player = player_choice("")
    board = full_check()
    while not (win_check(board) or place_marker(board)):
        display(board)
        win_check(player, board)
        player = win_check(player)
    display(board)

def display(board):

    clear_output()

    print('-------')
    print('|' + board[1] + '|' + board[2] +'|' + board[3] + '|')
    print('-------')
    print('|' + board[4] + '|' + board[5] +'|' + board[6] + '|')
    print('-------')
    print('|' + board[7] + '|' + board[8] +'|' + board[9] + '|')
    print('-------')

test = ['','x','o','x','o','x','o','x','o','x']
display(test)

## choosing the player -- deciding who goes first

import random

def choose_first():
    if random.randint(1,2) == 1:
        return 'player1'
    else:
        return 'player2'

choose_first()
'player1'

## Player1 choosing the marker

def marker_input():
    marker = ''

    while marker != 'X' and marker !='O':
        marker = input("Player1! Please choose 'X' or 'O' as your marker: ").upper()

    player1 = marker

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    print('Player1', player1)
    print('Player2', player2)

    return(player1, player2)

marker_input()

def space_check(board, position):
    return board[position] == ' '

test = ['','x','o','x','o','x','o','x','o','x']
space_check(test, 5)
False

def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Enter any position from [1-9]: '))

    return position

def place_marker(board, marker, position):
    board[position] = marker

def win_check (board, marker):
    return ((board[1] == board[2] == board[3] == marker) or (board[4] == board[5] == board[6] == marker) or 
           (board[7] == board[8] == board[9] == marker) or (board[1] == board[4] == board[7] == marker) or
           (board[2] == board[5] == board[8] == marker) or (board[3] == board[6] == board[9] == marker) or
           (board[1] == board[5] == board[9] == marker) or (board[3] == board[5] == board[7] == marker))

def full_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def replay():
    return input('Do you want to play again? Yes or No: ').upper().startswith('Y')

print('Welcome to Tic Tac Toe')

while True:
    Board = [' '] * 10
    player1_marker, player2_marker = marker_input()
    turn = choose_first()
    print(turn + ' will go first')

    play = input('Are you ready to play? Y/N:').upper()

    if play == 'Y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'player1':
            display(Board)
            position = player_choice(Board)
            print(player1_marker, 'player1 marker in function')
            place_marker(Board, player1_marker, position)

            if win_check(Board, player1_marker):
                display(Board)
                print('Congratulations! you have won the Game')
                game_on = False
            else:
                if full_check(Board):
                    display(Board)
                    print('Board is Full, Game is draw')
                    break
                else:
                    turn = 'player2'

        else:
            display(Board)
            position = player_choice(Board)
            place_marker(Board, player2_marker, position)

            if win_check(Board, player2_marker):
                display(Board)
                print('Congratulations! you have won the Game')
                game_on = False
            else:
                if full_check(Board):
                    display(Board)
                    print('Board is Full, Game is draw')
                    break
                else:
                    turn = 'player1'


    if not replay():
        break
if __name__ == "__main__":
    main()
