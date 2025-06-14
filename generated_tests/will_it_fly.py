def will_it_fly(q, w):
    if sum(q) > w:
        return False
    i, j = (0, len(q) - 1)
    while i < j:
        if q[i] != q[j]:
            return False
        i += 1
        j -= 1
    return True

import pytest

def test_sum_exceeds_w_returns_false():
    q = [3, 4, 5]
    w = 10
    expected = False
    assert will_it_fly(q, w) == expected

def test_sum_equals_w_and_palindrome_returns_true():
    q = [2, 3, 2]
    w = 7
    expected = True
    assert will_it_fly(q, w) == expected

def test_sum_less_than_w_but_not_palindrome_returns_false():
    q = [1, 2, 3]
    w = 10
    expected = False
    assert will_it_fly(q, w) == expected

def test_empty_list_with_w_zero_returns_true():
    q = []
    w = 0
    expected = True
    assert will_it_fly(q, w) == expected

def test_single_element_list_sum_equals_w_returns_true():
    q = [5]
    w = 5
    expected = True
    assert will_it_fly(q, w) == expected

def test_single_element_list_sum_exceeds_w_returns_false():
    q = [6]
    w = 5
    expected = False
    assert will_it_fly(q, w) == expected

def test_even_length_palindrome_sum_less_than_w_returns_true():
    q = [1, 2, 2, 1]
    w = 10
    expected = True
    assert will_it_fly(q, w) == expected

def test_even_length_non_palindrome_sum_less_than_w_returns_false():
    q = [1, 2, 3, 4]
    w = 15
    expected = False
    assert will_it_fly(q, w) == expected