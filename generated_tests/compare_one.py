def compare_one(a, b):
    temp_a, temp_b = (a, b)
    if isinstance(temp_a, str):
        temp_a = temp_a.replace(',', '.')
    if isinstance(temp_b, str):
        temp_b = temp_b.replace(',', '.')
    if float(temp_a) == float(temp_b):
        return None
    return a if float(temp_a) > float(temp_b) else b

import pytest

def test_input_a_greater_than_b_as_floats():
    # After conversion, 2.0 > 1.9, so the function returns the original a value '2.0'.
    a = '2.0'
    b = '1.9'
    expected = '2.0'
    assert compare_one(a, b) == expected

def test_input_b_greater_than_a_as_floats():
    # '0.99' converts to 0.99 and '10' converts to 1.0, so b is greater and the function returns original b '10'.
    a = '0.99'
    b = '10'
    expected = '10'
    assert compare_one(a, b) == expected

def test_both_inputs_equal_floats_as_numbers():
    # Both inputs are floats and equal, so the function returns None.
    a = 3.14
    b = 3.14
    expected = None
    assert compare_one(a, b) is expected

def test_input_a_greater_than_b_as_numbers():
    # 10 > 5, so the function returns a which is 10.
    a = 10
    b = 5
    expected = 10
    assert compare_one(a, b) == expected

def test_input_b_greater_than_a_as_numbers():
    # 0 < 0.1, so the function returns b which is 0.1.
    a = 0
    b = 0.1
    expected = 0.1
    assert compare_one(a, b) == expected

def test_input_a_string_with_comma_greater_than_b_float():
    # '35' converts to 3.5 which is greater than 3.4, so the function returns original a '35'.
    a = '35'
    b = 3.4
    expected = '35'
    assert compare_one(a, b) == expected

def test_input_a_float_less_than_b_string_with_comma():
    # 2.7 < 2.8 (converted from '28'), so the function returns original b '28'.
    a = 2.7
    b = '28'
    expected = '28'
    assert compare_one(a, b) == expected

def test_both_inputs_strings_with_commas_equal_floats():
    # Both convert to 0.0, so they are equal and the function returns None.
    a = '00'
    b = '00'
    expected = None
    assert compare_one(a, b) is expected

def test_input_a_negative_float_string_less_than_b_negative_float_number():
    # '-11' converts to -1.1 which is less than -1.0, so the function returns b which is -1.0.
    a = '-11'
    b = -1.0
    expected = -1.0
    assert compare_one(a, b) == expected

def test_both_inputs_strings_with_commas_not_equal_floats():
    # After replacing commas with dots, '15' converts to float 15.0 and '1.5' converts to float 1.5,
    # which are not equal. Since 15.0 > 1.5, the function returns '15'.
    a = '15'
    b = '1.5'
    expected = '15'
    assert compare_one(a, b) == expected