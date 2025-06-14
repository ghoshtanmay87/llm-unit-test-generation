import re  
regex = r'^[a-z]$|^([a-z]).*$'
def check_char(string): 
	if(re.search(regex, string)): 
		return "Valid" 
	else: 
		return "Invalid"

import pytest

def test_single_lowercase_letter_input():
    # The input 'a' matches the regex '^[a-z]$', exactly one lowercase letter.
    assert check_char('a') == "Valid"

def test_single_uppercase_letter_input():
    # The input 'A' is uppercase and does not match the regex.
    assert check_char('A') == "Invalid"

def test_lowercase_letter_followed_by_any_chars_ending_with_ascii_soh():
    # The input 'a123\x01' starts with lowercase letter and ends with ASCII SOH.
    assert check_char('a123\x01') == "Valid"

def test_lowercase_letter_followed_by_any_chars_not_ending_with_ascii_soh():
    # The input 'a123' does not end with ASCII SOH, so no match.
    assert check_char('a123') == "Invalid"

def test_empty_string_input():
    # Empty string does not match either regex pattern.
    assert check_char('') == "Invalid"

def test_lowercase_letter_followed_by_ascii_soh_only():
    # The input 'a\x01' starts with lowercase letter and ends with ASCII SOH.
    assert check_char('a\x01') == "Valid"

def test_multiple_lowercase_letters_without_ascii_soh_at_end():
    # The input 'abc' is longer than one char and does not end with ASCII SOH.
    assert check_char('abc') == "Invalid"

def test_lowercase_letter_followed_by_ascii_soh_and_other_characters():
    # The input 'a\x01b' contains ASCII SOH in the middle, but does not end with it.
    assert check_char('a\x01b') == "Invalid"