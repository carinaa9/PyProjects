# -*- coding: utf-8 -*-

# the computer has a secret number and user needs to find it

import random

def guess_number(x):
    random_number = random.randint(1,x) # returns a random number for us

# need to stop when our guess number equals the random number
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))

        if guess < random_number:
            print('It is too low! Sorry, try again')
        elif guess > random_number:
            print('It is too high! Sorry, try again')
    print(f'WOW!!!! You just guess the right number which is {random_number}.')

guess_number(10)








