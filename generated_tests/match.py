import re 
def match(text): 
		pattern = '[A-Z]+[a-z]+$'
		if re.search(pattern, text): 
				return('Yes') 
		else: 
				return('No')

import pytest

def test_text_ends_with_lowercase_preceded_by_uppercase():
    # Text ends with lowercase letters preceded by uppercase letters
    assert match("HELLOworld") == "Yes"

def test_text_all_uppercase_letters():
    # Text is all uppercase letters
    assert match("HELLO") == "No"

def test_text_all_lowercase_letters():
    # Text is all lowercase letters
    assert match("world") == "No"

def test_text_uppercase_followed_by_lowercase_not_at_end():
    # Text with uppercase letters followed by lowercase letters but not at the end
    assert match("HelloWorld123") == "No"

def test_text_uppercase_followed_by_lowercase_at_end():
    # Text with uppercase letters followed by lowercase letters at the end
    assert match("ABCdef") == "Yes"

def test_text_mixed_case_pattern_not_at_end():
    # Text with mixed case but pattern not at the end
    assert match("abcDEFghi") == "No"

def test_text_single_uppercase_followed_by_lowercase_at_end():
    # Text with single uppercase letter followed by lowercase letters at the end
    assert match("Aabc") == "Yes"

def test_text_uppercase_followed_by_digits_at_end():
    # Text with uppercase letters followed by digits at the end
    assert match("ABC123") == "No"