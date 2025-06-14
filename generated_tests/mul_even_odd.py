def mul_even_odd(list1):
    first_even = next((el for el in list1 if el%2==0),-1)
    first_odd = next((el for el in list1 if el%2!=0),-1)
    return (first_even*first_odd)

import pytest

def test_list_contains_both_even_and_odd_numbers():
    # The first even number is 2 and the first odd number is 3. Their product is 2*3=6.
    assert mul_even_odd([2, 3, 4, 5]) == 6

def test_list_contains_only_even_numbers():
    # The first even number is 4, but there is no odd number, so first_odd is -1. Product is 4*(-1) = -4.
    assert mul_even_odd([4, 6, 8]) == -4

def test_list_contains_only_odd_numbers():
    # The first odd number is 1, but there is no even number, so first_even is -1. Product is -1*1 = -1.
    assert mul_even_odd([1, 3, 5]) == -1

def test_list_contains_no_elements():
    # No even or odd numbers found, so first_even = -1 and first_odd = -1. Product is -1 * -1 = 1.
    assert mul_even_odd([]) == 1

def test_list_contains_zero_as_first_even_number_and_odd_numbers():
    # Zero is even and first even number is 0, first odd number is 7. Product is 0*7=0.
    assert mul_even_odd([0, 7, 9]) == 0

def test_list_contains_negative_even_and_odd_numbers():
    # First even is -2, first odd is -3. Product is -2 * -3 = 6.
    assert mul_even_odd([-2, -3, 4, 5]) == 6

def test_list_contains_even_number_after_odd_number():
    # First even is 8, first odd is 7. Product is 8*7=56.
    assert mul_even_odd([7, 8, 10]) == 56