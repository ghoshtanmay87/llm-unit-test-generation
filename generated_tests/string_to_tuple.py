def string_to_tuple(str1):
    result = tuple(x for x in str1 if not x.isspace()) 
    return result

import pytest

def test_string_to_tuple_no_spaces():
    # Convert a string with no spaces to a tuple of characters
    input_str = 'hello'
    expected = ('h', 'e', 'l', 'l', 'o')
    assert string_to_tuple(input_str) == expected

def test_string_to_tuple_with_spaces():
    # Convert a string with spaces to a tuple excluding spaces
    input_str = 'a b c'
    expected = ('a', 'b', 'c')
    assert string_to_tuple(input_str) == expected

def test_string_to_tuple_with_various_whitespace():
    # Convert a string with multiple types of whitespace characters
    input_str = 'x\ty\nz '
    expected = ('x', 't', 'y', 'n', 'z')
    assert string_to_tuple(input_str) == expected

def test_string_to_tuple_empty_string():
    # Convert an empty string to an empty tuple
    input_str = ''
    expected = ()
    assert string_to_tuple(input_str) == expected

def test_string_to_tuple_only_spaces():
    # Convert a string with only spaces to an empty tuple
    input_str = '     '
    expected = ()
    assert string_to_tuple(input_str) == expected