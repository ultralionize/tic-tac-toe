import os

theboard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

board_keys = []

for key in theboard:
    board_keys.append(key)


def print_board(board):
    os.system('cls')							# To clear the screen every-time the print_board is called
    print('\n\n\t\t ' + board['7'] + ' | ' + board['8'] + ' | ' + board['9'] + '\t\t\t\tPress 0 to quit')
    print('\t\t---+---+---')
    print('\t\t ' + board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('\t\t---+---+---')
    print('\t\t ' + board['1'] + ' | ' + board['2'] + ' | ' + board['3'])
