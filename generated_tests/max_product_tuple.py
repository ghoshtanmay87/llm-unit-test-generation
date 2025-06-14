def max_product_tuple(list1):
    result_max = max([abs(x * y) for x, y in list1] )
    return result_max

import pytest

def test_max_product_tuple_positive_and_negative_pairs():
    # Products: 6, -20, -6; absolute values: 6, 20, 6; max is 20
    input_data = [(2, 3), (-4, 5), (1, -6)]
    expected = 24
    assert max_product_tuple(input_data) == expected

def test_max_product_tuple_all_pairs_with_zero():
    # All products are zero, max absolute product is 0
    input_data = [(0, 5), (0, 0), (0, -3)]
    expected = 0
    assert max_product_tuple(input_data) == expected

def test_max_product_tuple_mixed_positive_and_negative_numbers():
    # Products: -56, 18, 12; absolute values: 56, 18, 12; max is 56
    input_data = [(7, -8), (-2, -9), (3, 4)]
    expected = 72
    assert max_product_tuple(input_data) == expected

def test_max_product_tuple_single_pair():
    # Only one product: 10 * -10 = -100; absolute value is 100
    input_data = [(10, -10)]
    expected = 100
    assert max_product_tuple(input_data) == expected

def test_max_product_tuple_all_positive_pairs():
    # Products: 2, 12, 30; max absolute product is 30
    input_data = [(1, 2), (3, 4), (5, 6)]
    expected = 30
    assert max_product_tuple(input_data) == expected