def lcs_of_three(X, Y, Z, m, n, o): 
	L = [[[0 for i in range(o+1)] for j in range(n+1)] 
		for k in range(m+1)] 
	for i in range(m+1): 
		for j in range(n+1): 
			for k in range(o+1): 
				if (i == 0 or j == 0 or k == 0): 
					L[i][j][k] = 0
				elif (X[i-1] == Y[j-1] and
					X[i-1] == Z[k-1]): 
					L[i][j][k] = L[i-1][j-1][k-1] + 1
				else: 
					L[i][j][k] = max(max(L[i-1][j][k], 
					L[i][j-1][k]), 
									L[i][j][k-1]) 
	return L[m][n][o]

import pytest

def test_all_strings_empty():
    # All three strings are empty
    X = ''
    Y = ''
    Z = ''
    m = 0
    n = 0
    o = 0
    expected = 0
    assert lcs_of_three(X, Y, Z, m, n, o) == expected

def test_one_string_empty_others_non_empty():
    # One string is empty, others non-empty
    X = 'abc'
    Y = 'abc'
    Z = ''
    m = 3
    n = 3
    o = 0
    expected = 0
    assert lcs_of_three(X, Y, Z, m, n, o) == expected

def test_all_strings_identical():
    # All three strings are identical
    X = 'abc'
    Y = 'abc'
    Z = 'abc'
    m = 3
    n = 3
    o = 3
    expected = 3
    assert lcs_of_three(X, Y, Z, m, n, o) == expected

def test_common_subsequence_length_4():
    # Common subsequence of length 4 among three strings
    X = 'abcdef'
    Y = 'abdfgh'
    Z = 'abdfxy'
    m = 6
    n = 6
    o = 6
    expected = 4
    assert lcs_of_three(X, Y, Z, m, n, o) == expected

def test_no_common_subsequence():
    # No common subsequence among three strings
    X = 'abc'
    Y = 'def'
    Z = 'ghi'
    m = 3
    n = 3
    o = 3
    expected = 0
    assert lcs_of_three(X, Y, Z, m, n, o) == expected

def test_partial_overlap_with_repeated_characters():
    # Partial overlap with repeated characters
    X = 'aabcc'
    Y = 'acbbc'
    Z = 'abccc'
    m = 5
    n = 5
    o = 5
    expected = 3
    assert lcs_of_three(X, Y, Z, m, n, o) == expected

def test_single_character_common_subsequence():
    # Single character common subsequence
    X = 'xyz'
    Y = 'ayz'
    Z = 'baz'
    m = 3
    n = 3
    o = 3
    expected = 2
    assert lcs_of_three(X, Y, Z, m, n, o) == expected

def test_common_subsequence_non_contiguous():
    # Common subsequence with non-contiguous characters
    X = 'abcdefg'
    Y = 'axbxcxdx'
    Z = 'abxcxdx'
    m = 7
    n = 8
    o = 7
    expected = 3
    assert lcs_of_three(X, Y, Z, m, n, o) == expected