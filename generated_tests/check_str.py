import re 
regex = '^[aeiouAEIOU][A-Za-z0-9_]*'
def check_str(string): 
	if(re.search(regex, string)): 
		return ("Valid") 
	else: 
		return ("Invalid")

import pytest

def test_string_starts_with_lowercase_vowel_and_only_letters():
    # The string starts with 'a', a lowercase vowel, and the rest are letters, matching the regex pattern.
    assert check_str("apple") == "Valid"

def test_string_starts_with_uppercase_vowel_and_letters_and_digits():
    # The string starts with 'O', an uppercase vowel, followed by letters and digits, which matches the regex.
    assert check_str("Orange123") == "Valid"

def test_string_starts_with_consonant():
    # The string starts with 'b', which is not a vowel, so it does not match the regex.
    assert check_str("banana") == "Invalid"

def test_string_starts_with_vowel_but_contains_special_characters():
    # The regex only checks the start of the string: it must start with a vowel followed by letters, digits, or underscores.
    # The '!' is after the matched part, so the regex still matches the start, making it valid.
    assert check_str("eagle!") == "Valid"

def test_string_starts_with_vowel_and_underscore():
    # The string starts with 'I', an uppercase vowel, followed by letters and underscores, which matches the regex.
    assert check_str("I_am_valid") == "Valid"

def test_empty_string_input():
    # Empty string does not match the regex because it requires at least one vowel at the start.
    assert check_str("") == "Invalid"

def test_string_starts_with_vowel_but_contains_space():
    # The regex matches only the start: 'A' followed by letters, digits, or underscores.
    # The space is after the matched part, so the regex matches, returning 'Valid'.
    assert check_str("A space") == "Valid"

def test_string_starts_with_vowel_followed_by_hyphen():
    # The regex matches from the start: 'e' followed by zero or more letters, digits, or underscores.
    # The hyphen is not part of the matched substring, but since re.search finds a match at the start, it returns 'Valid'.
    assert check_str("e-123") == "Valid"

def test_string_starts_with_vowel_and_only_one_character():
    # The string starts with 'U', an uppercase vowel, and the rest of the string is empty, which matches the regex.
    assert check_str("U") == "Valid"

def test_string_starts_with_digit():
    # The string starts with '1', which is not a vowel, so it does not match the regex.
    assert check_str("1apple") == "Invalid"