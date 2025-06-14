from typing import List

def string_xor(a: str, b: str) -> str:

    def xor(i, j):
        if i == j:
            return '0'
        else:
            return '1'
    return ''.join((xor(x, y) for x, y in zip(a, b)))

import pytest

def test_xor_identical_binary_strings():
    # XOR of two identical binary strings should be all zeros
    a = '1100'
    b = '1100'
    expected = '0000'
    assert string_xor(a, b) == expected

def test_xor_completely_different_binary_strings():
    # XOR of two completely different binary strings should be all ones
    a = '1010'
    b = '0101'
    expected = '1111'
    assert string_xor(a, b) == expected

def test_xor_mixed_matching_and_differing_bits():
    # XOR of strings with mixed matching and differing bits
    a = '1001'
    b = '1100'
    expected = '0101'
    assert string_xor(a, b) == expected

def test_xor_strings_length_greater_than_four():
    # XOR of strings with length greater than 4
    a = '111000'
    b = '101010'
    expected = '010010'
    assert string_xor(a, b) == expected

def test_xor_empty_strings():
    # XOR of empty strings should return empty string
    a = ''
    b = ''
    expected = ''
    assert string_xor(a, b) == expected

def test_xor_strings_different_lengths():
    # XOR of strings with different lengths compares only up to shortest length
    a = '101'
    b = '11011'
    expected = '011'
    assert string_xor(a, b) == expected