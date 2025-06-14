import re  
def remove(list): 
    pattern = '[0-9]'
    list = [re.sub(pattern, '', i) for i in list] 
    return list

import pytest

def test_remove_digits_from_strings_with_letters():
    # Remove all digits from a list of strings containing digits and letters
    input_list = ['a1', 'b2', 'c3']
    expected = ['a', 'b', 'c']
    assert remove(input_list) == expected

def test_remove_digits_from_strings_with_multiple_digits():
    # Remove digits from strings with multiple digits
    input_list = ['123abc456', '789def0']
    expected = ['abc', 'def']
    assert remove(input_list) == expected

def test_strings_with_no_digits_remain_unchanged():
    # Input list with strings containing no digits
    input_list = ['abc', 'def', 'ghi']
    expected = ['abc', 'def', 'ghi']
    assert remove(input_list) == expected

def test_empty_strings_and_digits():
    # Input list with empty strings and digits
    input_list = ['', '1', '2a3', '4']
    expected = ['', '', 'a', '']
    assert remove(input_list) == expected

def test_strings_with_special_characters_and_digits():
    # Input list with strings containing special characters and digits
    input_list = ['a1!b2@', '#3$4%']
    expected = ['a!b@', '#$%']
    assert remove(input_list) == expected