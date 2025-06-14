def is_sublist(l, s):
	sub_set = False
	if s == []:
		sub_set = True
	elif s == l:
		sub_set = True
	elif len(s) > len(l):
		sub_set = False
	else:
		for i in range(len(l)):
			if l[i] == s[0]:
				n = 1
				while (n < len(s)) and (l[i+n] == s[n]):
					n += 1				
				if n == len(s):
					sub_set = True
	return sub_set

import pytest

def test_empty_sublist_is_always_sublist():
    l = [1, 2, 3]
    s = []
    expected = True
    assert is_sublist(l, s) == expected

def test_sublist_equals_main_list():
    l = [1, 2, 3]
    s = [1, 2, 3]
    expected = True
    assert is_sublist(l, s) == expected

def test_sublist_longer_than_main_list():
    l = [1, 2]
    s = [1, 2, 3]
    expected = False
    assert is_sublist(l, s) == expected

def test_sublist_at_start_of_main_list():
    l = [1, 2, 3, 4]
    s = [1, 2]
    expected = True
    assert is_sublist(l, s) == expected

def test_sublist_in_middle_of_main_list():
    l = [5, 6, 7, 8, 9]
    s = [7, 8]
    expected = True
    assert is_sublist(l, s) == expected

def test_sublist_at_end_of_main_list():
    l = [10, 20, 30, 40]
    s = [30, 40]
    expected = True
    assert is_sublist(l, s) == expected

def test_sublist_elements_not_consecutive():
    l = [1, 3, 5, 7]
    s = [3, 7]
    expected = False
    assert is_sublist(l, s) == expected

def test_sublist_with_repeated_elements():
    l = [1, 2, 2, 3]
    s = [2, 2]
    expected = True
    assert is_sublist(l, s) == expected

def test_sublist_partial_match_fails_in_middle():
    l = [4, 5, 6, 7]
    s = [5, 7]
    expected = False
    assert is_sublist(l, s) == expected

def test_empty_main_list_with_non_empty_sublist():
    l = []
    s = [1]
    expected = False
    assert is_sublist(l, s) == expected