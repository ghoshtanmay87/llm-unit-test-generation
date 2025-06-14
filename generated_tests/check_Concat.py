def check_Concat(str1,str2):
    N = len(str1)
    M = len(str2)
    if (N % M != 0):
        return False
    for i in range(N):
        if (str1[i] != str2[i % M]):
            return False         
    return True

import pytest

def test_str1_repetition_of_str2_twice():
    # str1 is a repetition of str2 exactly twice
    str1 = "abcabc"
    str2 = "abc"
    expected = True
    assert check_Concat(str1, str2) == expected

def test_str1_length_not_multiple_of_str2_length():
    # str1 length is not a multiple of str2 length
    str1 = "abcab"
    str2 = "abc"
    expected = False
    assert check_Concat(str1, str2) == expected

def test_str1_repetition_of_str2_once():
    # str1 is a repetition of str2 exactly once
    str1 = "xyz"
    str2 = "xyz"
    expected = True
    assert check_Concat(str1, str2) == expected

def test_str1_repetition_with_mismatch():
    # str1 is a repetition of str2 multiple times with mismatch in characters
    str1 = "ababac"
    str2 = "ab"
    expected = False
    assert check_Concat(str1, str2) == expected

def test_str1_empty_str2_non_empty():
    # str1 is empty and str2 is non-empty
    str1 = ""
    str2 = "a"
    expected = True
    assert check_Concat(str1, str2) == expected

def test_both_str1_and_str2_empty():
    # both str1 and str2 are empty strings
    str1 = ""
    str2 = ""
    expected = False
    assert check_Concat(str1, str2) == expected

def test_str1_repetition_of_str2_three_times():
    # str1 is a repetition of str2 three times
    str1 = "xyzxyzxyz"
    str2 = "xyz"
    expected = True
    assert check_Concat(str1, str2) == expected

def test_str1_longer_not_repetition_of_str2():
    # str1 is longer but not a repetition of str2
    str1 = "abcdabcdabce"
    str2 = "abcd"
    expected = False
    assert check_Concat(str1, str2) == expected