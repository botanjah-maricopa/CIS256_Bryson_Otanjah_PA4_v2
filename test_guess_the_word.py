# Bryson Otanjah
# CIS256 Fall 2026
# Programming Assignment 4

from guess_the_word import WORDS, choose_word, process_guess

# checks that the result is in WORDs 100 times
def test_choose_word_comes_from_predefined_list():
    for _ in range(100):
        assert choose_word(WORDS) in WORDS

# verify correct guess is marked correct 
def test_correct_guess_returns_true():
    word = 'house'
    guessed = set()
    assert process_guess(word, 'u', guessed) == 'correct'
    assert 'u' in guessed

# verify incorrect guess is marked incorrect
def test_incorrect_guess_processed_correctly():
    guessed = set()
    assert process_guess('condo', 'a', guessed) == 'incorrect'
    assert 'a' in guessed