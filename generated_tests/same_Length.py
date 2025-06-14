def same_Length(A,B): 
    while (A > 0 and B > 0): 
        A = A / 10; 
        B = B / 10; 
    if (A == 0 and B == 0): 
        return True; 
    return False;

import pytest

def test_same_length_both_numbers_same_digits():
    # Both numbers have the same number of digits
    A = 1234
    B = 5678
    expected = True
    assert same_Length(A, B) == expected

def test_same_length_A_has_more_digits_than_B():
    # A has more digits than B
    A = 12345
    B = 678
    expected = False
    assert same_Length(A, B) == expected

def test_same_length_B_has_more_digits_than_A():
    # B has more digits than A
    A = 12
    B = 3456
    expected = False
    assert same_Length(A, B) == expected

def test_same_length_both_numbers_zero():
    # Both numbers are zero
    A = 0
    B = 0
    expected = True
    assert same_Length(A, B) == expected

def test_same_length_one_zero_other_nonzero():
    # One number is zero, the other is non-zero
    A = 0
    B = 1
    expected = False
    assert same_Length(A, B) == expected

def test_same_length_both_numbers_one_digit():
    # Both numbers have one digit
    A = 7
    B = 9
    expected = True
    assert same_Length(A, B) == expected

def test_same_length_large_numbers_same_length():
    # Large numbers with same length
    A = 1000000000
    B = 9999999999
    expected = True
    assert same_Length(A, B) == expected

def test_same_length_large_numbers_different_lengths():
    # Large numbers with different lengths
    A = 100000000
    B = 9999999999
    expected = False
    assert same_Length(A, B) == expected