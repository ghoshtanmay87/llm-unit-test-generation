def longest_common_subsequence(X, Y, m, n): 
    if m == 0 or n == 0: 
       return 0 
    elif X[m-1] == Y[n-1]: 
       return 1 + longest_common_subsequence(X, Y, m-1, n-1) 
    else: 
       return max(longest_common_subsequence(X, Y, m, n-1), longest_common_subsequence(X, Y, m-1, n))

import pytest

def test_both_strings_empty():
    X = ''
    Y = ''
    m = 0
    n = 0
    expected = 0
    assert longest_common_subsequence(X, Y, m, n) == expected

def test_one_string_empty_other_non_empty():
    X = 'ABC'
    Y = ''
    m = 3
    n = 0
    expected = 0
    assert longest_common_subsequence(X, Y, m, n) == expected

def test_identical_strings():
    X = 'ABC'
    Y = 'ABC'
    m = 3
    n = 3
    expected = 3
    assert longest_common_subsequence(X, Y, m, n) == expected

def test_no_common_characters():
    X = 'ABC'
    Y = 'DEF'
    m = 3
    n = 3
    expected = 0
    assert longest_common_subsequence(X, Y, m, n) == expected

def test_partial_match_with_subsequence():
    X = 'AGGTAB'
    Y = 'GXTXAYB'
    m = 6
    n = 7
    expected = 4
    assert longest_common_subsequence(X, Y, m, n) == expected

def test_repeated_characters_with_partial_overlap():
    X = 'AABBA'
    Y = 'ABABA'
    m = 5
    n = 5
    expected = 4
    assert longest_common_subsequence(X, Y, m, n) == expected

def test_single_character_match():
    X = 'A'
    Y = 'A'
    m = 1
    n = 1
    expected = 1
    assert longest_common_subsequence(X, Y, m, n) == expected

def test_single_character_no_match():
    X = 'A'
    Y = 'B'
    m = 1
    n = 1
    expected = 0
    assert longest_common_subsequence(X, Y, m, n) == expected