def find_Odd_Pair(A,N) : 
    oddPair = 0
    for i in range(0,N) :  
        for j in range(i+1,N) :  
            if ((A[i] ^ A[j]) % 2 != 0):  
                oddPair+=1  
    return oddPair

import pytest

def test_find_odd_pair_mixed_even_odd():
    # Find number of pairs with odd XOR in a list of mixed even and odd numbers
    A = [1, 2, 3, 4]
    N = 4
    expected = 4
    assert find_Odd_Pair(A, N) == expected

def test_find_odd_pair_all_even():
    # Find number of pairs with odd XOR in a list of all even numbers
    A = [2, 4, 6, 8]
    N = 4
    expected = 0
    assert find_Odd_Pair(A, N) == expected

def test_find_odd_pair_all_odd():
    # Find number of pairs with odd XOR in a list of all odd numbers
    A = [1, 3, 5, 7]
    N = 4
    expected = 0
    assert find_Odd_Pair(A, N) == expected

def test_find_odd_pair_single_element():
    # Find number of pairs with odd XOR in a list with one element
    A = [1]
    N = 1
    expected = 0
    assert find_Odd_Pair(A, N) == expected

def test_find_odd_pair_two_elements_one_odd_one_even():
    # Find number of pairs with odd XOR in a list with two elements, one odd and one even
    A = [2, 3]
    N = 2
    expected = 1
    assert find_Odd_Pair(A, N) == expected

def test_find_odd_pair_two_elements_both_even():
    # Find number of pairs with odd XOR in a list with two elements, both even
    A = [2, 4]
    N = 2
    expected = 0
    assert find_Odd_Pair(A, N) == expected

def test_find_odd_pair_two_elements_both_odd():
    # Find number of pairs with odd XOR in a list with two elements, both odd
    A = [1, 3]
    N = 2
    expected = 0
    assert find_Odd_Pair(A, N) == expected

def test_find_odd_pair_larger_list_mixed_parity():
    # Find number of pairs with odd XOR in a larger list with mixed parity
    A = [10, 15, 20, 25, 30]
    N = 5
    expected = 6
    assert find_Odd_Pair(A, N) == expected