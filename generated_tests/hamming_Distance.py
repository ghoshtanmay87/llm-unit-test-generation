def hamming_Distance(n1,n2) : 
    x = n1 ^ n2  
    setBits = 0
    while (x > 0) : 
        setBits += x & 1
        x >>= 1
    return setBits

import pytest

def test_hamming_distance_identical_numbers():
    # Calculate Hamming distance for two identical numbers
    n1 = 5
    n2 = 5
    expected = 0
    assert hamming_Distance(n1, n2) == expected

def test_hamming_distance_differ_by_one_bit():
    # Calculate Hamming distance for numbers differing by one bit
    n1 = 4
    n2 = 5
    expected = 1
    assert hamming_Distance(n1, n2) == expected

def test_hamming_distance_differ_by_multiple_bits():
    # Calculate Hamming distance for numbers differing by multiple bits
    n1 = 1
    n2 = 4
    expected = 2
    assert hamming_Distance(n1, n2) == expected

def test_hamming_distance_zero_and_number():
    # Calculate Hamming distance for zero and a number
    n1 = 0
    n2 = 7
    expected = 3
    assert hamming_Distance(n1, n2) == expected

def test_hamming_distance_large_numbers_multiple_bits():
    # Calculate Hamming distance for large numbers with multiple differing bits
    n1 = 29
    n2 = 15
    expected = 2
    assert hamming_Distance(n1, n2) == expected