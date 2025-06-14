def is_Sub_Array(A,B,n,m): 
    i = 0; j = 0; 
    while (i < n and j < m):  
        if (A[i] == B[j]): 
            i += 1; 
            j += 1; 
            if (j == m): 
                return True;  
        else: 
            i = i - j + 1; 
            j = 0;       
    return False;

import pytest

def test_subarray_B_at_start_of_A():
    A = [1, 2, 3, 4, 5]
    B = [1, 2, 3]
    n = 5
    m = 3
    assert is_Sub_Array(A, B, n, m) is True

def test_subarray_B_in_middle_of_A():
    A = [5, 6, 7, 8, 9]
    B = [7, 8]
    n = 5
    m = 2
    assert is_Sub_Array(A, B, n, m) is True

def test_B_not_subarray_of_A():
    A = [1, 2, 3, 4, 5]
    B = [2, 4]
    n = 5
    m = 2
    assert is_Sub_Array(A, B, n, m) is False

def test_B_empty_subarray():
    A = [1, 2, 3]
    B = []
    n = 3
    m = 0
    assert is_Sub_Array(A, B, n, m) is False

def test_B_equals_A():
    A = [4, 5, 6]
    B = [4, 5, 6]
    n = 3
    m = 3
    assert is_Sub_Array(A, B, n, m) is True

def test_B_longer_than_A():
    A = [1, 2]
    B = [1, 2, 3]
    n = 2
    m = 3
    assert is_Sub_Array(A, B, n, m) is False

def test_B_single_element_present_in_A():
    A = [10, 20, 30]
    B = [20]
    n = 3
    m = 1
    assert is_Sub_Array(A, B, n, m) is True

def test_B_single_element_not_present_in_A():
    A = [10, 20, 30]
    B = [40]
    n = 3
    m = 1
    assert is_Sub_Array(A, B, n, m) is False