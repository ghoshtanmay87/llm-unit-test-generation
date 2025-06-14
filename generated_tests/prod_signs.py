def prod_signs(arr):
    if not arr:
        return None
    prod = 0 if 0 in arr else (-1) ** len(list(filter(lambda x: x < 0, arr)))
    return prod * sum([abs(i) for i in arr])

import pytest

def test_empty_list_input_returns_none():
    # The function checks if the list is empty at the start and returns None immediately.
    assert prod_signs([]) is None

def test_list_contains_zero_returns_zero():
    # Since zero is in the list, prod is set to 0, so the final result is 0 regardless of other values.
    assert prod_signs([0, 1, -2, 3]) == 0

def test_all_positive_numbers_returns_sum_of_absolute_values():
    # No zero present, number of negative numbers is 0 (even), so prod = (-1)^0 = 1.
    # Sum of abs values is 6, so result is 1*6=6.
    assert prod_signs([1, 2, 3]) == 6

def test_even_number_of_negative_numbers_returns_positive_sum_of_absolute_values():
    # No zero present, number of negative numbers is 2 (even), so prod = 1.
    # Sum of abs values is 10, so result is 10.
    assert prod_signs([-1, 2, -3, 4]) == 10

def test_odd_number_of_negative_numbers_returns_negative_sum_of_absolute_values():
    # No zero present, number of negative numbers is 1 (odd), so prod = (-1)^1 = -1.
    # Sum of abs values is 6, so result is -6.
    assert prod_signs([-1, 2, 3]) == -6

def test_even_number_of_negative_numbers_returns_positive_sum_of_absolute_values_case2():
    # No zero present, number of negative numbers is 2 (even), so prod = (-1)^2 = 1.
    # Sum of abs values is 6, so result is 1*6=6.
    assert prod_signs([-1, 2, -3]) == 6