def histogram(test):
    dict1 = {}
    list1 = test.split(' ')
    t = 0
    for i in list1:
        if list1.count(i) > t and i != '':
            t = list1.count(i)
    if t > 0:
        for i in list1:
            if list1.count(i) == t:
                dict1[i] = t
    return dict1

import pytest

def test_histogram_multiple_words_one_most_frequent():
    input_data = 'apple banana apple orange banana apple'
    expected = {'apple': 3}
    assert histogram(input_data) == expected

def test_histogram_multiple_words_two_tie_highest_frequency():
    input_data = 'cat dog cat dog bird'
    expected = {'cat': 2, 'dog': 2}
    assert histogram(input_data) == expected

def test_histogram_all_unique_words():
    input_data = 'red blue green yellow'
    expected = {'red': 1, 'blue': 1, 'green': 1, 'yellow': 1}
    assert histogram(input_data) == expected

def test_histogram_empty_string():
    input_data = ''
    expected = {}
    assert histogram(input_data) == expected

def test_histogram_multiple_spaces_between_words():
    input_data = 'apple  apple   banana'
    expected = {'apple': 2}
    assert histogram(input_data) == expected

def test_histogram_single_word_repeated_multiple_times():
    input_data = 'test test test test'
    expected = {'test': 4}
    assert histogram(input_data) == expected

def test_histogram_words_with_trailing_spaces():
    input_data = 'one two three three '
    expected = {'three': 2}
    assert histogram(input_data) == expected