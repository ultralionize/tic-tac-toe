from board import *


# Checking for winning conditions.
# Checks whether either "X" or "O" are thrice in a straight line.
# If condition matches returns True(1), if not returns False(0).


def check_winner(player):
    triples = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['1', '5', '9'], ['7', '5', '3']]
    j = 0
    for i in range(5):              # iterate over list
        if theboard[triples[i][j]] == theboard[triples[i][j + 1]] == theboard[triples[i][j + 2]] != ' ':
            print('\nGame Over. ' + player + ' wins')
            return 1
    return 0

# To take input for the move
# Valid moves [0 .. 9].  Invalid moves [any other]
# [1 .. 9] for selecting block/position. [0] to quit


def take_input():
    choice = input()
    if choice == '0':                                               # if choice is to quit check
        ans = input("Do you want to quit ?(y/n) : ").lower()        # for confirmation.
        if ans in ['y', 'yes']:
            exit()
    else:
        return choice

# Checking for playing new game


def play_again():
    while 1:
        ans = input('\nDo you want to play again? (y/n) : ').lower()
        if ans in ['y', 'yes']:
            for values in board_keys:               # clear the board, if player
                theboard[values] = ' '              # wants to play again
            start()
        elif ans in ['n', 'no', '0']:
            exit()
        else:
            print('\nPlease enter y/n or yes/no')

# Checking for validity of the entered input and updating the board


def game_flow(count, player):
    while count < 10:                                       # only 9 valid moves allowed.
        print('\nIt\'s your turn ' + player + ' choose your move : ', end='')
        move = take_input()                                 # checking if move :
        if move in theboard:                                # is in the board
            if theboard[move] == ' ':                       # is available or already selected.
                theboard[move] = player
                count += 1
            else:
                print_board(theboard)
                print('\nBlock already selected, please select another place.\n', end='')
                continue

            print_board(theboard)
            if count >= 5:                                  # at-least 5 moves are required
                win = check_winner(player)                  # for determining the winner.
                if win == 1:                                # break if winner is determined
                    break

            if count == 9:                                  # if no winner is determined after 9
                print('\nIt\'s a tie')           # moves the declare as a tie.
                break

            if player == 'X':                               # toggle player after each selection.
                player = 'O'
            else:
                player = 'X'
        else:
            print_board(theboard)
            print('\nMove not valid, select a valid move.')

# start function calls all other functions of the game


def start():
    player = 'X'                                # first player is set as 'X' by default.
    count = 0
    print_board(theboard)
    game_flow(count, player)
    play_again()
