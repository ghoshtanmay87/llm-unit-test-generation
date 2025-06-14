def word_len(s): 
    s = s.split(' ')   
    for word in s:    
        if len(word)%2==0: 
            return True  
        else:
          return False

import pytest

def test_first_word_even_length():
    # Input string with first word having even length
    s = 'test odd even'
    expected = True
    assert word_len(s) == expected

def test_first_word_odd_length():
    # Input string with first word having odd length
    s = 'odd test even'
    expected = False
    assert word_len(s) == expected

def test_single_even_length_word():
    # Input string with single even-length word
    s = 'even'
    expected = True
    assert word_len(s) == expected

def test_single_odd_length_word():
    # Input string with single odd-length word
    s = 'odd'
    expected = False
    assert word_len(s) == expected

def test_first_word_empty_due_to_spaces():
    # Input string with first word empty due to multiple spaces
    s = '  even odd'
    expected = True
    assert word_len(s) == expected

def test_first_word_empty_string():
    # Input string with first word empty string
    s = ''
    expected = True
    assert word_len(s) == expected