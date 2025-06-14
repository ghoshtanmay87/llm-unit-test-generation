def unique_digits(x):
    odd_digit_elements = []
    for i in x:
        if all((int(c) % 2 == 1 for c in str(i))):
            odd_digit_elements.append(i)
    return sorted(odd_digit_elements)

import pytest

def test_all_elements_have_only_odd_digits():
    x = [135, 97531, 7]
    expected_output = [7, 135, 97531]
    assert unique_digits(x) == expected_output

def test_mixed_digits_with_some_numbers_containing_even_digits():
    x = [123, 135, 246, 97531, 802]
    expected_output = [135, 97531]
    assert unique_digits(x) == expected_output

def test_no_elements_with_all_odd_digits():
    x = [246, 802, 420, 68]
    expected_output = []
    assert unique_digits(x) == expected_output

def test_empty_input_list():
    x = []
    expected_output = []
    assert unique_digits(x) == expected_output

def test_single_element_with_all_odd_digits():
    x = [9]
    expected_output = [9]
    assert unique_digits(x) == expected_output

def test_single_element_with_even_digit():
    x = [4]
    expected_output = []
    assert unique_digits(x) == expected_output

def test_elements_with_multiple_digits_some_with_zeros():
    x = [101, 135, 707, 999, 808]
    expected_output = [135, 999]
    assert unique_digits(x) == expected_output