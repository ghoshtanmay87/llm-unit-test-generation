def unique_product(list_data):
    temp = list(set(list_data))
    p = 1
    for i in temp:
        p *= i
    return p

import pytest

def test_product_of_unique_elements_with_duplicates():
    # The unique elements are {2, 3, 4}. Their product is 2 * 3 * 4 = 24.
    input_data = [2, 3, 2, 4]
    expected = 24
    assert unique_product(input_data) == expected

def test_product_of_unique_elements_all_identical():
    # The unique element is {5}. The product is 5.
    input_data = [5, 5, 5, 5]
    expected = 5
    assert unique_product(input_data) == expected

def test_product_of_unique_elements_with_negative_and_positive():
    # The unique elements are {-1, 2, 3}. Their product is -1 * 2 * 3 = -6.
    input_data = [-1, 2, -1, 3]
    expected = -6
    assert unique_product(input_data) == expected

def test_product_of_unique_elements_empty_list():
    # There are no elements, so the product of unique elements defaults to 1 (multiplicative identity).
    input_data = []
    expected = 1
    assert unique_product(input_data) == expected

def test_product_of_unique_elements_with_zero():
    # The unique elements are {0, 1, 2, 3}. Since zero is included, the product is 0.
    input_data = [0, 1, 2, 2, 3]
    expected = 0
    assert unique_product(input_data) == expected