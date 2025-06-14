from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    sum_value = 0
    prod_value = 1
    for n in numbers:
        sum_value += n
        prod_value *= n
    return (sum_value, prod_value)

import pytest

def test_sum_product_empty_list_input():
    # Scenario: Empty list input
    # With no elements, sum starts at 0 and remains 0; product starts at 1 and remains 1 since no multiplication occurs.
    result = sum_product(numbers=[])
    assert result == (0, 1)

def test_sum_product_single_positive_number():
    # Scenario: Single positive number
    # Sum is 5 (only element), product is 5 (1 multiplied by 5).
    result = sum_product(numbers=[5])
    assert result == (5, 5)

def test_sum_product_multiple_positive_numbers():
    # Scenario: Multiple positive numbers
    # Sum is 1+2+3+4=10; product is 1*2*3*4=24.
    result = sum_product(numbers=[1, 2, 3, 4])
    assert result == (10, 24)

def test_sum_product_list_with_zero_included():
    # Scenario: List with zero included
    # Sum is 0+1+2=3; product is 0*1*2=0 because multiplication by zero yields zero.
    result = sum_product(numbers=[0, 1, 2])
    assert result == (3, 0)

def test_sum_product_list_with_negative_numbers():
    # Scenario: List with negative numbers
    # Sum is -1 + (-2) + (-3) = -6; product is (-1)*(-2)*(-3) = 2 * (-3) = -6.
    result = sum_product(numbers=[-1, -2, -3])
    assert result == (-6, -6)

def test_sum_product_list_with_mixed_positive_and_negative_numbers():
    # Scenario: List with mixed positive and negative numbers
    # Sum is 2 + (-3) + 4 = 3; product is 2 * (-3) * 4 = -24.
    result = sum_product(numbers=[2, -3, 4])
    assert result == (3, -24)

def test_sum_product_list_with_one_element_zero():
    # Scenario: List with one element zero
    # Sum is 0; product is 1 * 0 = 0.
    result = sum_product(numbers=[0])
    assert result == (0, 0)