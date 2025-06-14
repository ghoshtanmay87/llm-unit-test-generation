class Pair(object): 
	def __init__(self, a, b): 
		self.a = a 
		self.b = b 
def max_chain_length(arr, n): 
	max = 0
	mcl = [1 for i in range(n)] 
	for i in range(1, n): 
		for j in range(0, i): 
			if (arr[i].a > arr[j].b and
				mcl[i] < mcl[j] + 1): 
				mcl[i] = mcl[j] + 1
	for i in range(n): 
		if (max < mcl[i]): 
			max = mcl[i] 
	return max

import pytest

def test_single_pair_input():
    arr = [Pair(5, 24)]
    n = 1
    expected = 1
    assert max_chain_length(arr, n) == expected

def test_two_pairs_second_can_follow_first():
    arr = [Pair(5, 24), Pair(27, 40)]
    n = 2
    expected = 2
    assert max_chain_length(arr, n) == expected

def test_two_pairs_second_cannot_follow_first():
    arr = [Pair(5, 24), Pair(20, 40)]
    n = 2
    expected = 1
    assert max_chain_length(arr, n) == expected

def test_multiple_pairs_chain_length_3():
    arr = [Pair(5, 24), Pair(15, 25), Pair(27, 40), Pair(50, 60)]
    n = 4
    expected = 3
    assert max_chain_length(arr, n) == expected

def test_pairs_with_no_chaining_possible():
    arr = [Pair(5, 10), Pair(6, 9), Pair(7, 8)]
    n = 3
    expected = 1
    assert max_chain_length(arr, n) == expected

def test_pairs_with_longest_chain_5():
    arr = [Pair(1, 2), Pair(3, 4), Pair(5, 6), Pair(7, 8), Pair(9, 10)]
    n = 5
    expected = 5
    assert max_chain_length(arr, n) == expected

def test_pairs_with_some_overlapping_longest_chain_3():
    arr = [Pair(1, 5), Pair(2, 3), Pair(4, 6), Pair(7, 8)]
    n = 4
    expected = 3
    assert max_chain_length(arr, n) == expected