# -*- coding: utf-8 -*-

import random
import string
from words import words

#print(words)
## jogo da forca -- guessing the word through the letters
def get_valid_word(words):
    word = random.choice(words) # choose some random word from the list
    while "-" in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed

    lives = 5

    #guetting the user input
    while len(word_letters) > 0 and lives > 0:

        #letters used
        print(f'You have', lives, 'and you have used these letters: ', ' '.join(used_letters))

        #what the current word is
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: '.upper())
        if user_letter in alphabet-used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            else:
                lives = lives - 1 # takes one life if wrong
                print('Letter is not in the word.')

        elif user_letter in used_letters:
            print('\nYou have already used that character. Please try again.')

        else:
            print('\nThat is a invalid character. Please try again ')

    # when len(word_letters) == 0 or when lives == '0'
    if lives == 0:
        print('Sorry, your lives are over. The word was', word)
    else:
        print('You guessed the word', word, '!!!')

hangman()