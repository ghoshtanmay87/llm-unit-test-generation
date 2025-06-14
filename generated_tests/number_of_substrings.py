def number_of_substrings(str): 
	str_len = len(str); 
	return int(str_len * (str_len + 1) / 2);

import pytest

def test_number_of_substrings_empty_string():
    # Calculate number of substrings for an empty string
    result = number_of_substrings(str='')
    assert result == 0

def test_number_of_substrings_single_character():
    # Calculate number of substrings for a single character string
    result = number_of_substrings(str='a')
    assert result == 1

def test_number_of_substrings_two_characters():
    # Calculate number of substrings for a two character string
    result = number_of_substrings(str='ab')
    assert result == 3

def test_number_of_substrings_three_characters():
    # Calculate number of substrings for a three character string
    result = number_of_substrings(str='abc')
    assert result == 6

def test_number_of_substrings_longer_string():
    # Calculate number of substrings for a longer string
    result = number_of_substrings(str='hello')
    assert result == 15