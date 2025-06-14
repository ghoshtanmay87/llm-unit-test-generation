def tuple_int_str(tuple_str):
    result = tuple((int(x[0]), int(x[1])) for x in tuple_str)
    return result

import pytest

def test_convert_tuple_of_two_strings_representing_digits_to_tuple_of_two_integers():
    # scenario: Convert tuple of two strings representing digits to tuple of two integers
    input_value = ('1', '2')
    expected_output = (1, 2)
    assert tuple_int_str(input_value) == expected_output

def test_convert_tuple_of_two_strings_representing_two_digit_numbers_to_tuple_of_two_integers():
    # scenario: Convert tuple of two strings representing two-digit numbers to tuple of two integers
    input_value = ('10', '20')
    expected_output = ((1, 0), (2, 0))
    assert tuple_int_str(input_value) == expected_output

def test_convert_tuple_of_two_strings_each_with_two_digits_to_tuple_of_tuples_of_integers():
    # scenario: Convert tuple of two strings each with two digits to tuple of tuples of integers
    input_value = ('34', '56')
    expected_output = ((3, 4), (5, 6))
    assert tuple_int_str(input_value) == expected_output

def test_convert_tuple_of_two_strings_with_single_digit_characters_raises_index_error():
    # scenario: Convert tuple of two strings with single digit characters to tuple of tuples of integers
    input_value = ('7', '8')
    with pytest.raises(IndexError):
        tuple_int_str(input_value)

def test_convert_tuple_of_two_strings_with_negative_digits_raises_value_error():
    # scenario: Convert tuple of two strings with negative digits to tuple of tuples of integers
    input_value = ('-1', '-2')
    with pytest.raises(ValueError):
        tuple_int_str(input_value)