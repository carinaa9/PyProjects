# -*- coding: utf-8 -*-

import random

def play():
    user = input("Hi! Just use 'r' for rock, 'p' for paper, 's' for scissors \n").lower()

    # computer is also going to choose 
    computer = random.choice(['r', 'p', 's'])

    # rules to win the game

    if user == computer: # has the same choice
        return 'Ups! It\'s a tie'
    
    if win(user, computer):
        return 'Congrat\'s! You won!'
    return 'Sorry! You lost'


def win(player, opponent):
    # return true if the player wins
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())
