# -*- coding: utf-8 -*-

import random
import math

class Player:

    def __init__(self, letter) -> None:
        # letter will be x or o
        self.letter = letter

    # players get next move
    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    ''' builds on top of this bass player object'''
    def __init__(self, letter) -> None:
        super().__init__(letter) # player

    def get_move(self, game):
        #gets a random spot that is empty
        square = random.choice(game.available_moves())  
        return square

class HumanPlayer(Player):
    '''our superclass is still player'''
    def __init__(self, letter) -> None:
        super().__init__(letter)

    def get_move(self, game):
        # human choose a spot
        valid_square = False
        value = None
        while not valid_square:
            square = input(self.letter + '\'s tunr. Choose a move (0-8): ')

            try:
                value = int(square)
                if value not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return value


class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            # begging : every squares are available
            square = random.choice(game.available_moves())
        else:
            # get the square based off the minimax algorithm
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        # find the best move 
        max_player = self.letter  # yourself
        other_player = 'O' if player == 'X' else 'X'

        # first we want to check if the previous move is a winner
        if state.current_winner == other_player:
            return {'position': None, 
                    'score': 1 * (state.num_empty_squares() + 1) 
                    if other_player == max_player 
                    else -1 * (state.num_empty_squares() + 1)}

        elif not state.empty_squares(): # no empty squares
            return {'position': None, 
                    'score': 0}

        if player == max_player:
            best = {'position': None,
                    'score': - math.inf}  # each score should maximize
        else:
            best = {'position': None,  
                    'score': math.inf}  # each score should minimize
        
        for possible_move in state.available_moves():
            # make a kove, try that spot
            state.make_move(possible_move, player)
            # recurse using minimax
            sim_score = self.minimax(state, other_player)  # simulate a game after making that move

            # undo move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move  # this represents the move optimal next move

            # update the dictionaries if necessary
            if player == max_player:  # X is max player
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best