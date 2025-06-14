def count_X(tup, x): 
    count = 0
    for ele in tup: 
        if (ele == x): 
            count = count + 1
    return count

import pytest

def test_count_occurrences_multiple_times():
    # Count occurrences of x when x appears multiple times in the tuple
    tup = (1, 2, 3, 2, 4, 2)
    x = 2
    expected = 3
    assert count_X(tup, x) == expected

def test_count_occurrences_once():
    # Count occurrences of x when x appears once in the tuple
    tup = (5, 6, 7, 8)
    x = 7
    expected = 1
    assert count_X(tup, x) == expected

def test_count_occurrences_not_present():
    # Count occurrences of x when x does not appear in the tuple
    tup = (9, 10, 11)
    x = 4
    expected = 0
    assert count_X(tup, x) == expected

def test_count_occurrences_empty_tuple():
    # Count occurrences of x in an empty tuple
    tup = ()
    x = 1
    expected = 0
    assert count_X(tup, x) == expected

def test_count_occurrences_all_elements_are_x():
    # Count occurrences of x when all elements in the tuple are x
    tup = (3, 3, 3, 3)
    x = 3
    expected = 4
    assert count_X(tup, x) == expected

def test_count_occurrences_with_different_data_types():
    # Count occurrences of x when tuple contains different data types and x is a string
    tup = (1, 'a', 2, 'a', 3)
    x = 'a'
    expected = 2
    assert count_X(tup, x) == expected

def test_count_occurrences_with_none_values():
    # Count occurrences of x when tuple contains None values and x is None
    tup = (None, 1, None, 2, None)
    x = None
    expected = 3
    assert count_X(tup, x) == expected