def reverse_Array_Upto_K(input, k): 
  return (input[k-1::-1] + input[k:])

import pytest

def test_reverse_first_k_elements_less_than_length():
    # Scenario: Reverse first k elements where k is less than length of input
    input_list = [1, 2, 3, 4, 5]
    k = 3
    expected = [3, 2, 1, 4, 5]
    assert reverse_Array_Upto_K(input_list, k) == expected

def test_reverse_entire_array_when_k_equals_length():
    # Scenario: Reverse entire array when k equals length of input
    input_list = [10, 20, 30, 40]
    k = 4
    expected = [40, 30, 20, 10]
    assert reverse_Array_Upto_K(input_list, k) == expected

def test_reverse_first_element_only_k_is_1():
    # Scenario: Reverse first element only when k is 1
    input_list = [7, 8, 9]
    k = 1
    expected = [7, 8, 9]
    assert reverse_Array_Upto_K(input_list, k) == expected

def test_reverse_first_k_elements_k_is_2_longer_list():
    # Scenario: Reverse first k elements where k is 2 in a longer list
    input_list = [5, 4, 3, 2, 1]
    k = 2
    expected = [4, 5, 3, 2, 1]
    assert reverse_Array_Upto_K(input_list, k) == expected

def test_reverse_first_k_elements_k_is_0_edge_case():
    # Scenario: Reverse first k elements where k is 0 (edge case)
    input_list = [1, 2, 3]
    k = 0
    expected = [3, 2, 1]
    assert reverse_Array_Upto_K(input_list, k) == expected

def test_reverse_first_k_elements_k_greater_than_length_edge_case():
    # Scenario: Reverse first k elements where k is greater than length of input (edge case)
    input_list = [1, 2, 3]
    k = 5
    expected = [3, 2, 1]
    assert reverse_Array_Upto_K(input_list, k) == expected