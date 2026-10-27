# Bryson Otanjah
# CIS256 Fall 2026
# Programming Assignment 4

# full disclosure, I thought I was saving to git throughout
# but I didn't realize how to use it so it was just saving locally
# so this is an ai approximation of my code development, 
# I understand if the score reflect that this isn't a true
# representation of my progress

import random

# initial word list and attempt limit
WORDS = ['house', 'apartment', 'condo']
MAX_ATTEMPTS = 5


def choose_word(words):
    """Return one randomly selected word."""
    return random.choice(words)


def play_game(words=WORDS, max_attempts=MAX_ATTEMPTS):
    """Initial game loop: choose a word and collect letter guesses."""
    word = choose_word(words)
    guessed_letters = set()
    attempts_left = max_attempts

    print('Guess the Word! The Game!')

    while attempts_left > 0:
        guess = input('Guess a single letter: ').lower()
        guessed_letters.add(guess)

        if guess in word:
            print("That's a good guess!")
        else:
            attempts_left -= 1
            print('Wrong!')

        print(f'Guessed letters: {guessed_letters}')
        print(f'Attempts left: {attempts_left}')


if __name__ == "__main__":
    play_game()
