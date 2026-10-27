# Bryson Otanjah
# CIS256 Fall 2026
# Programming Assignment 4
# Sorry, I couldn't figure out git in time

import random 


# list of words for random to select 
WORDS = ['house', 'apartment', 'condo']

# number of incorrect guesses allowed
MAX_ATTEMPTS = 5

# return a word from the WORDS list
def choose_word(words):
    return random.choice(words)

# unknown letters are returned as '_'
def display_word(word, guessed_letters):
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)

# process a guess and updated guessed_letters 
def process_guess(word, guess, guessed_letters):
    guess = guess.lower()
    
    if len(guess) != 1: # must be exactly 1
        return 'error 1'
    if not guess.isalpha(): # must be a letter
        return 'error 2'
    if guess in guessed_letters: # must be a unique quess 
        return 'error 3'
    
    guessed_letters.add(guess)
    
    # returns correct or incorrect, 'in' covers all matching letters
    return 'correct' if guess in word else 'incorrect'

# true if every letter guessed
def is_word_guessed(word, guessed_letters):
    return all(letter in guessed_letters for letter in word)

# run a round, returns true for a win and false for a loss
def play_game(words=WORDS, max_attempts=MAX_ATTEMPTS):
    word = choose_word(words)
    guessed_letters = set()
    attempts_left = max_attempts
    
    print('Guess the Word! The Game!')
    # loop until the word is complete or attempts exhausted
    while attempts_left > 0 and not is_word_guessed(word, guessed_letters):
        print(f'Word: {display_word(word, guessed_letters)}')
        print(f'Attempts left: {attempts_left}')
        guess = input('Guess a single letter: ')
        
        result = process_guess(word, guess, guessed_letters)\
        
        if result == 'error 1':
            print('Enter only a single character.')
        elif result == 'error 2':
            print('Enter an alphabetical character only.')
        elif result == 'error 3':
            print('Repeat guess')
        elif result == 'correct':
            print("That's a good guess!")
        else:
            attempts_left -= 1 # costs one attempt only when incrrect
            print('Wrong!')
        
    if is_word_guessed(word, guessed_letters):
        print(f'Congratulations! You guessed the word: {word}')
        return True
    
    print(f'You win!')
    return False

if __name__ == "__main__":
    play_game()