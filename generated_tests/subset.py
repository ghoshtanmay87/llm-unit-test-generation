def subset(ar, n): 
    res = 0
    ar.sort() 
    for i in range(0, n) : 
        count = 1
        for i in range(n - 1): 
            if ar[i] == ar[i + 1]: 
                count+=1
            else: 
                break 
        res = max(res, count)  
    return res

import pytest

def test_all_elements_are_distinct():
    ar = [1, 2, 3, 4, 5]
    n = 5
    expected_output = 1
    assert subset(ar, n) == expected_output

def test_all_elements_are_the_same():
    ar = [7, 7, 7, 7]
    n = 4
    expected_output = 4
    assert subset(ar, n) == expected_output

def test_some_duplicates_at_the_start():
    ar = [2, 2, 3, 4, 5]
    n = 5
    expected_output = 2
    assert subset(ar, n) == expected_output

def test_duplicates_not_at_the_start():
    ar = [1, 3, 3, 3, 5]
    n = 5
    expected_output = 1
    assert subset(ar, n) == expected_output

def test_empty_array():
    ar = []
    n = 0
    expected_output = 0
    assert subset(ar, n) == expected_output

def test_single_element_array():
    ar = [10]
    n = 1
    expected_output = 1
    assert subset(ar, n) == expected_output