# -*- coding: utf-8 -*-

# define the game 

import math
import time
from player import GeniusComputerPlayer
from player import HumanPlayer, RandomComputerPlayer


class TicTacToe:
    ''' build a board to the game'''

    def __init__(self) -> None:
        # 3x3 board
        self.board = [' ' for _ in range(9)] # we are gonna use an index for each space 
        self.current_winner = None

    @staticmethod
    def make_board():
        # mekes an empty board
        return [' ' for _ in range(9)]

    def print_board(self):
        # 012 its the first row, 345 second and 678 third
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
        
    @staticmethod
    def print_board_nums():
        # j*3 is 0, 1 and 2 -- index of the board
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def empty_squares(self):
        # check if there are any empty squares on the board
        return ' ' in self.board

    def num_empty_squares(self):
        # count the number of spaces in the board
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ': # if that spaces is empty
            self.board[square] = letter # letter of the player (computer or human)
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # check the row
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3:(row_ind+1)*3] # list of the items in the row
        
        # print('row', row)
        
        if all([spot == letter for spot in row]):
            return True

        # check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # check diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            # print('diag1', diagonal1)
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            # print('diag2', diagonal2)
            if all([spot == letter for spot in diagonal2]):
                return True
        return False

    

    def available_moves(self):
        #moves = []
        
        #for (i, spot) in enumerate(self.board):
            # its gonna do this:
            # ['x', 'o', 'x'] --> [(0, 'x'), (1, 'o'), (2, 'x')]
            #if spot == ' ':
                #moves.append(i) #is a empty space
        #return moves

        #or
        return [i for i, spot in enumerate(self.board) if spot == ' ']



def play(game, x_player, o_player, print_game = True):
    if print_game:
        game.print_board_nums()

    letter = 'X' # starting letter for default
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        
        if game.make_move(square, letter):

            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board() # new representation of the board
                print('')

        
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter  # ends the loop and exits the game

            # after we made our move, we need to alternate letters
            letter = 'O' if letter == 'X' else 'X'  # switches player

        time.sleep(1)

    if print_game:
        print('It\'s a tie!')



if __name__ == '__main__':

    # simple game and easier game
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    game = TicTacToe()
    play(game, x_player, o_player, print_game=True)

    # game against the genius computer so its more dificult
    x_player = HumanPlayer('X')
    o_player = GeniusComputerPlayer('O')
    game = TicTacToe()
    play(game, x_player, o_player, print_game=True)



