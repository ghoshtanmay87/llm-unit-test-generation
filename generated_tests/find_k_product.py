def get_product(val) : 
	res = 1
	for ele in val: 
		res *= ele 
	return res 
def find_k_product(test_list, K):
  res = get_product([sub[K] for sub in test_list])
  return (res)

import pytest

def test_product_elements_index_1():
    # Calculate product of elements at index K=1 in a list of lists
    test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    K = 1
    expected_output = 80
    assert find_k_product(test_list, K) == expected_output

def test_product_elements_index_0():
    # Calculate product of elements at index K=0 in a list of lists
    test_list = [[2, 3], [5, 6], [7, 8]]
    K = 0
    expected_output = 70
    assert find_k_product(test_list, K) == expected_output

def test_product_elements_index_2_with_negatives():
    # Calculate product of elements at index K=2 in a list of lists with negative numbers
    test_list = [[1, -2, 3], [4, 5, -6], [7, 8, 9]]
    K = 2
    expected_output = -162
    assert find_k_product(test_list, K) == expected_output

def test_product_elements_index_0_single_element_lists():
    # Calculate product of elements at index K=0 in a list of single-element lists
    test_list = [[10], [20], [30]]
    K = 0
    expected_output = 6000
    assert find_k_product(test_list, K) == expected_output

def test_product_elements_index_1_single_sublist():
    # Calculate product of elements at index K=1 in a list with one sublist
    test_list = [[3, 4, 5]]
    K = 1
    expected_output = 4
    assert find_k_product(test_list, K) == expected_output