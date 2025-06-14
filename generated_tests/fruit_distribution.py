def fruit_distribution(s, n):
    lis = list()
    for i in s.split(' '):
        if i.isdigit():
            lis.append(int(i))
    return n - sum(lis)

import pytest

def test_all_numbers_in_string_sum_less_than_n():
    s = '3 4 2'
    n = 15
    expected = 6
    assert fruit_distribution(s, n) == expected

def test_string_contains_non_digit_words_and_digits():
    s = 'apple 5 banana 3'
    n = 20
    expected = 12
    assert fruit_distribution(s, n) == expected

def test_string_contains_no_digits():
    s = 'apple banana orange'
    n = 10
    expected = 10
    assert fruit_distribution(s, n) == expected

def test_string_contains_digits_equal_to_n():
    s = '7 3'
    n = 10
    expected = 0
    assert fruit_distribution(s, n) == expected

def test_string_contains_digits_greater_than_n():
    s = '10 5 6'
    n = 15
    expected = -6
    assert fruit_distribution(s, n) == expected