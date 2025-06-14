def find_remainder(arr, lens, n): 
    mul = 1
    for i in range(lens):  
        mul = (mul * (arr[i] % n)) % n 
    return mul % n

import pytest

def test_remainder_product_small_positive_integers():
    arr = [2, 3, 4]
    lens = 3
    n = 5
    expected = 4
    assert find_remainder(arr, lens, n) == expected

def test_remainder_product_all_zeros():
    arr = [0, 0, 0]
    lens = 3
    n = 7
    expected = 0
    assert find_remainder(arr, lens, n) == expected

def test_remainder_product_mod_one_always_zero():
    arr = [10, 20, 30]
    lens = 3
    n = 1
    expected = 0
    assert find_remainder(arr, lens, n) == expected

def test_remainder_product_single_element_array():
    arr = [7]
    lens = 1
    n = 3
    expected = 1
    assert find_remainder(arr, lens, n) == expected

def test_remainder_product_large_numbers_and_modulus():
    arr = [1000, 2000, 3000]
    lens = 3
    n = 13
    expected = 12
    assert find_remainder(arr, lens, n) == expected

def test_remainder_product_with_negative_numbers():
    arr = [-1, -2, -3]
    lens = 3
    n = 5
    expected = 4
    assert find_remainder(arr, lens, n) == expected

def test_remainder_product_lens_less_than_array_length():
    arr = [1, 2, 3, 4, 5]
    lens = 3
    n = 7
    expected = 6
    assert find_remainder(arr, lens, n) == expected