from collections import Counter 
def count_Occurrence(tup, lst): 
    count = 0
    for item in tup: 
        if item in lst: 
            count+= 1 
    return count

import pytest

def test_count_occurrences_all_elements_in_list():
    tup = (1, 2, 3)
    lst = [1, 2, 3, 4, 5]
    expected = 3
    assert count_Occurrence(tup, lst) == expected

def test_count_occurrences_some_elements_in_list():
    tup = (1, 2, 6)
    lst = [1, 2, 3, 4, 5]
    expected = 2
    assert count_Occurrence(tup, lst) == expected

def test_count_occurrences_no_elements_in_list():
    tup = (7, 8, 9)
    lst = [1, 2, 3, 4, 5]
    expected = 0
    assert count_Occurrence(tup, lst) == expected

def test_count_occurrences_repeated_elements_in_tuple():
    tup = (1, 1, 2, 2, 3)
    lst = [1, 2, 3]
    expected = 5
    assert count_Occurrence(tup, lst) == expected

def test_count_occurrences_empty_tuple():
    tup = ()
    lst = [1, 2, 3]
    expected = 0
    assert count_Occurrence(tup, lst) == expected

def test_count_occurrences_empty_list():
    tup = (1, 2, 3)
    lst = []
    expected = 0
    assert count_Occurrence(tup, lst) == expected

def test_count_occurrences_mixed_types():
    tup = (1, 'a', 3)
    lst = [1, 2, 'a', 'b']
    expected = 2
    assert count_Occurrence(tup, lst) == expected