def string_to_md5(text):
    import hashlib
    return hashlib.md5(text.encode('ascii')).hexdigest() if text else None

import pytest

def test_string_to_md5_simple_lowercase():
    # Convert a simple lowercase ASCII string to its MD5 hash
    input_text = 'hello'
    expected = '5d41402abc4b2a76b9719d911017c592'
    assert string_to_md5(input_text) == expected

def test_string_to_md5_empty_string_returns_none():
    # Convert an empty string input to None
    input_text = ''
    expected = None
    assert string_to_md5(input_text) is expected

def test_string_to_md5_numeric_string():
    # Convert a numeric string to its MD5 hash
    input_text = '123456'
    expected = 'e10adc3949ba59abbe56e057f20f883e'
    assert string_to_md5(input_text) == expected

def test_string_to_md5_mixed_case_ascii():
    # Convert a string with mixed case ASCII letters to its MD5 hash
    input_text = 'OpenAI'
    expected = '0523b13262b12c215d8009938f5c14f1'
    assert string_to_md5(input_text) == expected

def test_string_to_md5_special_ascii_characters():
    # Convert a string with special ASCII characters to its MD5 hash
    input_text = '!@#$%^&*()'
    expected = '05b28d17a7b6e7024b6e5d8cc43a8bf7'
    assert string_to_md5(input_text) == expected