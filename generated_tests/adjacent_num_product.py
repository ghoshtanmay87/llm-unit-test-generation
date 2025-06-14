def adjacent_num_product(list_nums):
    return max(a*b for a, b in zip(list_nums, list_nums[1:]))

import pytest

def test_max_product_positive_integers():
    # Find max product of adjacent numbers in a list of positive integers
    input_list = [1, 2, 3, 4, 5]
    expected = 20
    assert adjacent_num_product(input_list) == expected

def test_max_product_negative_and_positive_integers():
    # Find max product when list contains negative and positive integers
    input_list = [-1, 3, -2, 4, -5]
    expected = -3
    assert adjacent_num_product(input_list) == expected

def test_max_product_with_zeros():
    # Find max product in a list with zeros
    input_list = [0, 2, 0, 3, 0]
    expected = 0
    assert adjacent_num_product(input_list) == expected

def test_max_product_single_element_raises_value_error():
    # Find max product in a list with one element
    input_list = [7]
    with pytest.raises(ValueError):
        adjacent_num_product(input_list)

def test_max_product_two_elements():
    # Find max product in a list with two elements
    input_list = [10, -10]
    expected = -100
    assert adjacent_num_product(input_list) == expected

def test_max_product_all_negative_numbers():
    # Find max product in a list with all negative numbers
    input_list = [-3, -6, -2, -8]
    expected = 18
    assert adjacent_num_product(input_list) == expected

def test_max_product_mixed_large_numbers():
    # Find max product in a list with mixed large numbers
    input_list = [1000, 2000, -3000, 4000]
    expected = 2000000
    assert adjacent_num_product(input_list) == expected