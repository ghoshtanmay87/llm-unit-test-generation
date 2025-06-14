import re 
regex = '[a-zA-z0-9]$'
def check_alphanumeric(string): 
	if(re.search(regex, string)): 
		return ("Accept") 
	else: 
		return ("Discard")

import pytest

def test_string_ends_with_lowercase_letter():
    # The string 'hello' ends with 'o' which is a lowercase letter, so it matches and returns 'Accept'.
    assert check_alphanumeric("hello") == "Accept"

def test_string_ends_with_uppercase_letter():
    # The string 'HELLO' ends with 'O', an uppercase letter, so it returns 'Accept'.
    assert check_alphanumeric("HELLO") == "Accept"

def test_string_ends_with_digit():
    # The string 'test123' ends with '3', a digit, so it returns 'Accept'.
    assert check_alphanumeric("test123") == "Accept"

def test_string_ends_with_special_character():
    # The string 'hello!' ends with '!', which is not a letter or digit, so it returns 'Discard'.
    assert check_alphanumeric("hello!") == "Discard"

def test_string_ends_with_space():
    # The string 'hello ' ends with a space character, so it returns 'Discard'.
    assert check_alphanumeric("hello ") == "Discard"

def test_empty_string_input():
    # An empty string has no characters, so it returns 'Discard'.
    assert check_alphanumeric("") == "Discard"

def test_string_ends_with_lowercase_z():
    # The string 'abcxyz' ends with 'z', a lowercase letter, so it returns 'Accept'.
    assert check_alphanumeric("abcxyz") == "Accept"

def test_string_ends_with_uppercase_Z():
    # The string 'ABCXYZ' ends with 'Z', an uppercase letter, so it returns 'Accept'.
    assert check_alphanumeric("ABCXYZ") == "Accept"

def test_string_ends_with_newline_character():
    # The string 'hello\n' ends with a newline character, so it returns 'Discard'.
    assert check_alphanumeric("hello\n") == "Discard"

def test_string_ends_with_digit_zero():
    # The string 'number0' ends with '0', a digit, so it returns 'Accept'.
    assert check_alphanumeric("number0") == "Accept"