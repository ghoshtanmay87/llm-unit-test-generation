def string_list_to_tuple(str1):
    result = tuple(x for x in str1 if not x.isspace()) 
    return result

import pytest

def test_string_list_to_tuple_no_spaces():
    # Convert a string with no spaces to a tuple of characters
    input_str = 'hello'
    expected = ('h', 'e', 'l', 'l', 'o')
    assert string_list_to_tuple(input_str) == expected

def test_string_list_to_tuple_with_spaces():
    # Convert a string with spaces to a tuple excluding spaces
    input_str = 'a b c'
    expected = ('a', 'b', 'c')
    assert string_list_to_tuple(input_str) == expected

def test_string_list_to_tuple_with_tabs_and_newlines():
    # Convert a string with tabs and newlines to a tuple excluding all whitespace
    input_str = 'x\ty\nz'
    expected = ('x', 'y', 'z')
    assert string_list_to_tuple(input_str) == expected

def test_string_list_to_tuple_empty_string():
    # Convert an empty string to an empty tuple
    input_str = ''
    expected = ()
    assert string_list_to_tuple(input_str) == expected

def test_string_list_to_tuple_only_whitespace():
    # Convert a string with only whitespace characters to an empty tuple
    input_str = ' \t\n'
    expected = ()
    assert string_list_to_tuple(input_str) == expected

def test_string_list_to_tuple_mixed_whitespace_and_chars():
    # Convert a string with mixed whitespace and non-whitespace characters
    input_str = '  a \tb\nc  '
    expected = ('a', 'b', 'c')
    assert string_list_to_tuple(input_str) == expected