def super_seq(X, Y, m, n):
	if (not m):
		return n
	if (not n):
		return m
	if (X[m - 1] == Y[n - 1]):
		return 1 + super_seq(X, Y, m - 1, n - 1)
	return 1 + min(super_seq(X, Y, m - 1, n),	super_seq(X, Y, m, n - 1))

import pytest

def test_both_strings_empty():
    X = ''
    Y = ''
    m = 0
    n = 0
    expected = 0
    assert super_seq(X, Y, m, n) == expected

def test_one_string_empty_other_non_empty():
    X = 'abc'
    Y = ''
    m = 3
    n = 0
    expected = 3
    assert super_seq(X, Y, m, n) == expected

def test_one_string_empty_other_non_empty_reverse():
    X = ''
    Y = 'xyz'
    m = 0
    n = 3
    expected = 3
    assert super_seq(X, Y, m, n) == expected

def test_strings_with_no_common_characters():
    X = 'abc'
    Y = 'def'
    m = 3
    n = 3
    expected = 6
    assert super_seq(X, Y, m, n) == expected

def test_strings_with_some_common_characters():
    X = 'abac'
    Y = 'cab'
    m = 4
    n = 3
    expected = 5
    assert super_seq(X, Y, m, n) == expected

def test_strings_are_identical():
    X = 'algorithm'
    Y = 'algorithm'
    m = 9
    n = 9
    expected = 9
    assert super_seq(X, Y, m, n) == expected

def test_strings_with_partial_overlap():
    X = 'geek'
    Y = 'eke'
    m = 4
    n = 3
    expected = 5
    assert super_seq(X, Y, m, n) == expected