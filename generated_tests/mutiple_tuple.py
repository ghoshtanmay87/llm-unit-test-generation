def mutiple_tuple(nums):
    temp = list(nums)
    product = 1 
    for x in temp:
        product *= x
    return product

import pytest

def test_product_of_positive_integers():
    # Calculate product of positive integers
    result = mutiple_tuple((1, 2, 3, 4))
    assert result == 24

def test_product_with_zero_element():
    # Calculate product with a zero element
    result = mutiple_tuple((5, 0, 10))
    assert result == 0

def test_product_of_single_element_tuple():
    # Calculate product of a single element tuple
    result = mutiple_tuple((7,))
    assert result == 7

def test_product_of_empty_tuple():
    # Calculate product of an empty tuple
    result = mutiple_tuple(())
    assert result == 1

def test_product_of_negative_and_positive_integers():
    # Calculate product of negative and positive integers
    result = mutiple_tuple((-1, 2, -3))
    assert result == 6