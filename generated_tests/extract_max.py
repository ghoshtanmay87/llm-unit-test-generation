import re 
def extract_max(input): 
	numbers = re.findall('\d+',input) 
	numbers = map(int,numbers) 
	return max(numbers)

import pytest

def test_extract_max_multiple_numbers():
    # Extract maximum number from a string with multiple numbers
    input_str = 'The 3 little pigs built 5 houses and 12 barns'
    expected = 12
    assert extract_max(input_str) == expected

def test_extract_max_single_number():
    # Extract maximum number from a string with a single number
    input_str = 'There is only 7 apples'
    expected = 7
    assert extract_max(input_str) == expected

def test_extract_max_numbers_embedded_in_words():
    # Extract maximum number from a string with numbers embedded in words
    input_str = 'abc123def45gh6'
    expected = 123
    assert extract_max(input_str) == expected

def test_extract_max_numbers_separated_by_spaces():
    # Extract maximum number from a string with numbers separated by spaces
    input_str = '10 20 30 40 50'
    expected = 50
    assert extract_max(input_str) == expected

def test_extract_max_no_numbers():
    # Extract maximum number from a string with no numbers
    input_str = 'No digits here!'
    # The function raises ValueError on empty input list for max()
    with pytest.raises(ValueError):
        extract_max(input_str)

def test_extract_max_numbers_with_leading_zeros():
    # Extract maximum number from a string with numbers having leading zeros
    input_str = 'Values are 007, 0008, and 00009'
    expected = 9
    assert extract_max(input_str) == expected