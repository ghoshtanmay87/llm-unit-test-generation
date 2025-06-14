from itertools import zip_longest, chain, tee
def exchange_elements(lst):
    lst1, lst2 = tee(iter(lst), 2)
    return list(chain.from_iterable(zip_longest(lst[1::2], lst[::2])))

import pytest

def test_exchange_elements_even_number_of_elements():
    # Scenario: Exchange elements in a list with even number of elements
    input_lst = [1, 2, 3, 4]
    expected = [2, 1, 4, 3]
    assert exchange_elements(input_lst) == expected

def test_exchange_elements_odd_number_of_elements():
    # Scenario: Exchange elements in a list with odd number of elements
    input_lst = [10, 20, 30, 40, 50]
    expected = [20, 10, 40, 30, 50]
    assert exchange_elements(input_lst) == expected

def test_exchange_elements_single_element():
    # Scenario: Exchange elements in a list with a single element
    input_lst = [99]
    expected = [99]
    assert exchange_elements(input_lst) == expected

def test_exchange_elements_empty_list():
    # Scenario: Exchange elements in an empty list
    input_lst = []
    expected = []
    assert exchange_elements(input_lst) == expected

def test_exchange_elements_two_elements():
    # Scenario: Exchange elements in a list with two elements
    input_lst = [7, 8]
    expected = [8, 7]
    assert exchange_elements(input_lst) == expected