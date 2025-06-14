import re
def start_withp(words):
 for w in words:
        m = re.match("(P\w+)\W(P\w+)", w)
        if m:
            return m.groups()

import pytest

def test_two_p_words_separated_by_hyphen():
    words = ['Pineapple-Pie', 'Pear-Peach']
    expected = ('Pineapple', 'Pie')
    assert start_withp(words) == expected

def test_two_p_words_separated_by_space():
    words = ['Panda Panda', 'Pineapple-Pie']
    expected = ('Panda', 'Panda')
    assert start_withp(words) == expected

def test_two_p_words_separated_by_comma():
    words = ['Pear,Pie', 'Pineapple-Pie']
    expected = ('Pear', 'Pie')
    assert start_withp(words) == expected

def test_no_matching_strings():
    words = ['Apple-Pie', 'Banana-Pie']
    expected = None
    assert start_withp(words) is expected

def test_one_p_word_then_matching_string():
    words = ['Pineapple', 'Pear-Pie']
    expected = ('Pear', 'Pie')
    assert start_withp(words) == expected

def test_two_p_words_separated_by_underscore():
    words = ['Pear_Pie', 'Pineapple-Pie']
    expected = ('Pineapple', 'Pie')
    assert start_withp(words) == expected

def test_two_p_words_separated_by_multiple_non_word_chars():
    words = ['Pineapple--Pie', 'Pear-Pie']
    expected = ('Pear', 'Pie')
    assert start_withp(words) == expected

def test_empty_input_list():
    words = []
    expected = None
    assert start_withp(words) is expected