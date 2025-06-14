def length_Of_Last_Word(a): 
    l = 0
    x = a.strip() 
    for i in range(len(x)): 
        if x[i] == " ": 
            l = 0
        else: 
            l += 1
    return l

import pytest

def test_length_of_last_word_multiple_words_single_spaces():
    # Input string with multiple words separated by single spaces
    input_str = "Hello World"
    expected = 5
    assert length_Of_Last_Word(input_str) == expected

def test_length_of_last_word_trailing_spaces():
    # Input string with trailing spaces
    input_str = "   fly me   to   the moon  "
    expected = 4
    assert length_Of_Last_Word(input_str) == expected

def test_length_of_last_word_single_word_no_spaces():
    # Input string with a single word and no spaces
    input_str = "Hello"
    expected = 5
    assert length_Of_Last_Word(input_str) == expected

def test_length_of_last_word_multiple_spaces_between_words():
    # Input string with multiple spaces between words
    input_str = "a  b  c"
    expected = 1
    assert length_Of_Last_Word(input_str) == expected

def test_length_of_last_word_only_spaces():
    # Input string with only spaces
    input_str = "     "
    expected = 0
    assert length_Of_Last_Word(input_str) == expected

def test_length_of_last_word_one_word_trailing_spaces():
    # Input string with one word and trailing spaces
    input_str = "test   "
    expected = 4
    assert length_Of_Last_Word(input_str) == expected

def test_length_of_last_word_multiple_words_leading_spaces():
    # Input string with multiple words and leading spaces
    input_str = "   openAI is great"
    expected = 5
    assert length_Of_Last_Word(input_str) == expected

def test_length_of_last_word_single_character_word():
    # Input string with a single character word
    input_str = "x"
    expected = 1
    assert length_Of_Last_Word(input_str) == expected