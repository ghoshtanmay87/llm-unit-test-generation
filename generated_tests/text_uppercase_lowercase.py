import re
def text_uppercase_lowercase(text):
        patterns = '[A-Z]+[a-z]+$'
        if re.search(patterns, text):
                return 'Found a match!'
        else:
                return ('Not matched!')

import pytest

def test_text_ends_with_uppercase_followed_by_lowercase_letters():
    # Text ends with uppercase letters followed by lowercase letters
    input_text = 'HELLOworld'
    expected = 'Found a match!'
    assert text_uppercase_lowercase(input_text) == expected

def test_text_ends_with_only_uppercase_letters():
    # Text ends with only uppercase letters
    input_text = 'HELLO'
    expected = 'Not matched!'
    assert text_uppercase_lowercase(input_text) == expected

def test_text_ends_with_only_lowercase_letters():
    # Text ends with only lowercase letters
    input_text = 'world'
    expected = 'Not matched!'
    assert text_uppercase_lowercase(input_text) == expected

def test_text_with_uppercase_followed_by_lowercase_not_at_end():
    # Text with uppercase followed by lowercase letters not at the end
    input_text = 'HELLOworld123'
    expected = 'Not matched!'
    assert text_uppercase_lowercase(input_text) == expected

def test_text_with_uppercase_followed_by_lowercase_at_end_with_mixed_case_inside():
    # Text with uppercase followed by lowercase letters at the end with mixed case inside
    input_text = 'abcXYZabc'
    expected = 'Found a match!'
    assert text_uppercase_lowercase(input_text) == expected

def test_text_with_lowercase_followed_by_uppercase_letters_at_end():
    # Text with lowercase followed by uppercase letters at the end
    input_text = 'abcxyzABC'
    expected = 'Not matched!'
    assert text_uppercase_lowercase(input_text) == expected

def test_text_with_uppercase_and_lowercase_but_not_in_required_order_at_end():
    # Text with uppercase and lowercase letters but not in required order at the end
    input_text = 'abcAbC'
    expected = 'Not matched!'
    assert text_uppercase_lowercase(input_text) == expected

def test_text_with_single_uppercase_followed_by_single_lowercase_at_end():
    # Text with single uppercase letter followed by single lowercase letter at the end
    input_text = 'Aq'
    expected = 'Found a match!'
    assert text_uppercase_lowercase(input_text) == expected

def test_empty_string_input():
    # Empty string input
    input_text = ''
    expected = 'Not matched!'
    assert text_uppercase_lowercase(input_text) == expected

def test_text_with_uppercase_followed_by_lowercase_in_middle_not_at_end():
    # Text with uppercase followed by lowercase letters in the middle but not at the end
    input_text = 'HELLOworld!'
    expected = 'Not matched!'
    assert text_uppercase_lowercase(input_text) == expected