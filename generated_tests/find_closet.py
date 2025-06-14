import sys 

def find_closet(A, B, C, p, q, r): 
	diff = sys.maxsize 
	res_i = 0
	res_j = 0
	res_k = 0
	i = 0
	j = 0
	k = 0
	while(i < p and j < q and k < r): 
		minimum = min(A[i], min(B[j], C[k])) 
		maximum = max(A[i], max(B[j], C[k])); 
		if maximum-minimum < diff: 
			res_i = i 
			res_j = j 
			res_k = k 
			diff = maximum - minimum; 
		if diff == 0: 
			break
		if A[i] == minimum: 
			i = i+1
		elif B[j] == minimum: 
			j = j+1
		else: 
			k = k+1
	return A[res_i],B[res_j],C[res_k]

import pytest

def test_find_closest_triplet_distinct_elements():
    A = [1, 4, 10]
    B = [2, 15, 20]
    C = [10, 12]
    expected = (10, 15, 10)
    result = find_closet(A, B, C, len(A), len(B), len(C))
    assert result == expected

def test_find_closest_triplet_overlapping_values():
    A = [5, 8, 10]
    B = [6, 9, 15]
    C = [7, 12, 16]
    expected = (8, 9, 7)
    result = find_closet(A, B, C, len(A), len(B), len(C))
    assert result == expected

def test_find_closest_triplet_identical_elements():
    A = [1, 2, 3]
    B = [1, 2, 3]
    C = [1, 2, 3]
    expected = (1, 1, 1)
    result = find_closet(A, B, C, len(A), len(B), len(C))
    assert result == expected

def test_find_closest_triplet_one_array_single_element():
    A = [1, 5, 10]
    B = [2, 3, 6]
    C = [4]
    expected = (5, 3, 4)
    result = find_closet(A, B, C, len(A), len(B), len(C))
    assert result == expected

def test_find_closest_triplet_negative_and_positive_numbers():
    A = [-10, -5, 0]
    B = [-6, 1, 3]
    C = [-2, 4, 8]
    expected = (0, 1, -2)
    result = find_closet(A, B, C, len(A), len(B), len(C))
    assert result == expected