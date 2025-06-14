def find_even_Pair(A,N): 
    evenPair = 0
    for i in range(0,N): 
        for j in range(i+1,N): 
            if ((A[i] ^ A[j]) % 2 == 0): 
                evenPair+=1
    return evenPair;

import pytest

def test_all_elements_even_numbers():
    # All elements are even numbers
    A = [2, 4, 6, 8]
    N = 4
    expected = 6
    assert find_even_Pair(A, N) == expected

def test_mixed_even_and_odd_numbers():
    # Mixed even and odd numbers
    A = [1, 2, 3, 4]
    N = 4
    expected = 2
    assert find_even_Pair(A, N) == expected

def test_single_element_array():
    # Single element array
    A = [10]
    N = 1
    expected = 0
    assert find_even_Pair(A, N) == expected

def test_empty_array():
    # Empty array
    A = []
    N = 0
    expected = 0
    assert find_even_Pair(A, N) == expected

def test_two_elements_one_even_one_odd():
    # Array with two elements, one even and one odd
    A = [2, 3]
    N = 2
    expected = 0
    assert find_even_Pair(A, N) == expected

def test_two_even_elements():
    # Array with two even elements
    A = [2, 4]
    N = 2
    expected = 1
    assert find_even_Pair(A, N) == expected

def test_two_odd_elements():
    # Array with two odd elements
    A = [1, 3]
    N = 2
    expected = 1
    assert find_even_Pair(A, N) == expected

def test_all_elements_odd_numbers():
    # All elements are odd numbers
    A = [1, 3, 5, 7]
    N = 4
    expected = 6
    assert find_even_Pair(A, N) == expected