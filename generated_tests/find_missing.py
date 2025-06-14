def find_missing(ar,N): 
    l = 0
    r = N - 1
    while (l <= r):  
        mid = (l + r) / 2
        mid= int (mid) 
        if (ar[mid] != mid + 1 and ar[mid - 1] == mid): 
            return (mid + 1)  
        elif (ar[mid] != mid + 1): 
            r = mid - 1 
        else: 
            l = mid + 1
    return (-1)

import pytest

def test_missing_number_in_middle():
    ar = [1, 2, 3, 5, 6]
    N = 5
    expected = 4
    assert find_missing(ar, N) == expected

def test_no_missing_number_last_element():
    ar = [1, 2, 3, 4, 5]
    N = 5
    expected = -1
    assert find_missing(ar, N) == expected

def test_missing_number_near_start():
    ar = [1, 3, 4, 5, 6]
    N = 5
    expected = 2
    assert find_missing(ar, N) == expected

def test_single_element_no_missing():
    ar = [1]
    N = 1
    expected = -1
    assert find_missing(ar, N) == expected

def test_missing_first_element_not_detected():
    ar = [2, 3, 4, 5, 6]
    N = 5
    expected = -1
    assert find_missing(ar, N) == expected

def test_single_element_missing_first_number_not_detected():
    ar = [2]
    N = 1
    expected = -1
    assert find_missing(ar, N) == expected