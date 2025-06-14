def swap_count(s):
	chars = s
	count_left = 0
	count_right = 0
	swap = 0
	imbalance = 0; 
	for i in range(len(chars)):
		if chars[i] == '[':
			count_left += 1
			if imbalance > 0:
				swap += imbalance
				imbalance -= 1
		elif chars[i] == ']':
			count_right += 1
			imbalance = (count_right - count_left) 
	return swap

import pytest

def test_all_brackets_balanced_and_properly_ordered():
    s = '[][]'
    expected = 0
    assert swap_count(s) == expected

def test_one_pair_of_brackets_reversed():
    s = ']['
    expected = 1
    assert swap_count(s) == expected

def test_multiple_reversed_pairs():
    s = ']]][[['
    expected = 9
    assert swap_count(s) == expected

def test_nested_balanced_brackets():
    s = '[[[]]]'
    expected = 0
    assert swap_count(s) == expected

def test_alternating_brackets_starting_with_right_bracket():
    s = '][[]]['
    expected = 2
    assert swap_count(s) == expected