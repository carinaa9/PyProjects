# -*- coding: utf-8 -*-
import random

# I have a secret number and I want that the computer guessing
def computer_guess(x):
    low = 1
    high = x
    feedback = '' # theres no high and low at the begining

    while feedback != 'c':
        if low != high:
             guess = random.randint(low, high)
        
        else:
            guess = high # or low, its equal
        
        feedback = input(f'Is {guess} too high (H), too low (L) or correct (C)??? ').lower()

        if feedback == 'h':
            high = guess - 1
        if feedback == 'l':
            low = guess + 1

    print('WOW!!! I guess your number!!')

computer_guess(10)