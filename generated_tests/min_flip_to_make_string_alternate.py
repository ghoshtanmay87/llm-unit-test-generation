def make_flip(ch): 
	return '1' if (ch == '0') else '0'
def get_flip_with_starting_charcter(str, expected): 
	flip_count = 0
	for i in range(len( str)): 
		if (str[i] != expected): 
			flip_count += 1
		expected = make_flip(expected) 
	return flip_count 
def min_flip_to_make_string_alternate(str): 
	return min(get_flip_with_starting_charcter(str, '0'),get_flip_with_starting_charcter(str, '1'))

import pytest

def test_all_characters_same_zero():
    # All characters are the same and equal to '0'
    input_str = '0000'
    expected = 2
    assert min_flip_to_make_string_alternate(input_str) == expected

def test_all_characters_same_one():
    # All characters are the same and equal to '1'
    input_str = '1111'
    expected = 2
    assert min_flip_to_make_string_alternate(input_str) == expected

def test_already_alternating_starting_with_zero():
    # String is already alternating starting with '0'
    input_str = '0101'
    expected = 0
    assert min_flip_to_make_string_alternate(input_str) == expected

def test_already_alternating_starting_with_one():
    # String is already alternating starting with '1'
    input_str = '1010'
    expected = 0
    assert min_flip_to_make_string_alternate(input_str) == expected

def test_alternating_with_one_char_flipped():
    # String with alternating pattern but one character flipped
    input_str = '0110'
    expected = 1
    assert min_flip_to_make_string_alternate(input_str) == expected

def test_all_alternating_except_last_char():
    # String with all characters alternating except last character
    input_str = '0100'
    expected = 1
    assert min_flip_to_make_string_alternate(input_str) == expected

def test_empty_string():
    # Empty string input
    input_str = ''
    expected = 0
    assert min_flip_to_make_string_alternate(input_str) == expected

def test_single_character_zero():
    # Single character string '0'
    input_str = '0'
    expected = 0
    assert min_flip_to_make_string_alternate(input_str) == expected

def test_single_character_one():
    # Single character string '1'
    input_str = '1'
    expected = 0
    assert min_flip_to_make_string_alternate(input_str) == expected

def test_long_alternating_starting_with_zero():
    # Long string with alternating pattern starting with '0'
    input_str = '0101010101'
    expected = 0
    assert min_flip_to_make_string_alternate(input_str) == expected

def test_long_alternating_starting_with_one():
    # Long string with alternating pattern starting with '1'
    input_str = '1010101010'
    expected = 0
    assert min_flip_to_make_string_alternate(input_str) == expected

def test_long_string_all_zeros():
    # Long string with all '0's
    input_str = '0000000000'
    expected = 5
    assert min_flip_to_make_string_alternate(input_str) == expected

def test_long_string_all_ones():
    # Long string with all '1's
    input_str = '1111111111'
    expected = 5
    assert min_flip_to_make_string_alternate(input_str) == expected