def Repeat(x): 
    _size = len(x) 
    repeated = [] 
    for i in range(_size): 
        k = i + 1
        for j in range(k, _size): 
            if x[i] == x[j] and x[i] not in repeated: 
                repeated.append(x[i]) 
    return repeated

import pytest

def test_repeat_no_repeated_elements():
    # Input list with no repeated elements
    x = [1, 2, 3, 4, 5]
    expected = []
    assert Repeat(x) == expected

def test_repeat_one_repeated_element_twice():
    # Input list with one repeated element appearing twice
    x = [1, 2, 2, 3]
    expected = [2]
    assert Repeat(x) == expected

def test_repeat_multiple_repeated_elements():
    # Input list with multiple repeated elements
    x = [1, 2, 3, 2, 1, 4]
    expected = [1, 2]
    assert Repeat(x) == expected

def test_repeat_elements_repeated_more_than_twice():
    # Input list with repeated elements appearing more than twice
    x = [5, 5, 5, 6, 6]
    expected = [5, 6]
    assert Repeat(x) == expected

def test_repeat_all_elements_same():
    # Input list with all elements the same
    x = [7, 7, 7, 7]
    expected = [7]
    assert Repeat(x) == expected

def test_repeat_repeated_elements_separated_by_unique():
    # Input list with repeated elements separated by unique elements
    x = [1, 3, 1, 4, 3, 5]
    expected = [1, 3]
    assert Repeat(x) == expected

def test_repeat_repeated_strings():
    # Input list with repeated strings
    x = ['a', 'b', 'a', 'c', 'b']
    expected = ['a', 'b']
    assert Repeat(x) == expected

def test_repeat_empty_list():
    # Input list with no elements (empty list)
    x = []
    expected = []
    assert Repeat(x) == expected