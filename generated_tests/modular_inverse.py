def modular_inverse(arr, N, P):
	current_element = 0
	for i in range(0, N):
		if ((arr[i] * arr[i]) % P == 1):
			current_element = current_element + 1
	return current_element

import pytest

def test_count_elements_square_mod_p_equals_1_small_array():
    arr = [1, 2, 3, 4]
    N = 4
    P = 5
    expected = 2
    assert modular_inverse(arr, N, P) == expected

def test_no_elements_satisfy_condition_prime_p():
    arr = [2, 3, 5]
    N = 3
    P = 7
    expected = 0
    assert modular_inverse(arr, N, P) == expected

def test_all_elements_are_1():
    arr = [1, 1, 1]
    N = 3
    P = 10
    expected = 3
    assert modular_inverse(arr, N, P) == expected

def test_mixed_elements_larger_p_no_elements_satisfy():
    arr = [6, 7, 8, 9]
    N = 4
    P = 11
    expected = 0
    assert modular_inverse(arr, N, P) == expected

def test_elements_1_and_p_minus_1_satisfy():
    arr = [1, 10, 3]
    N = 3
    P = 11
    expected = 2
    assert modular_inverse(arr, N, P) == expected