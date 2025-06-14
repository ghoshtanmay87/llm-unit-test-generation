def camel_to_snake(text):
        import re
        str1 = re.sub('(.)([A-Z][a-z]+)', r'_', text)
        return re.sub('([a-z0-9])([A-Z])', r'_', str1).lower()

import pytest

def test_camel_to_snake_simple_camel_case_one_uppercase():
    # Convert simple camel case string with one uppercase letter in the middle
    input_text = 'CamelCase'
    expected = 'camel_case'
    assert camel_to_snake(input_text) == expected

def test_camel_to_snake_multiple_uppercase_letters_middle():
    # Convert camel case string with multiple uppercase letters in the middle
    input_text = 'ThisIsATest'
    expected = 'this_is_a_test'
    assert camel_to_snake(input_text) == expected

def test_camel_to_snake_consecutive_uppercase_letters():
    # Convert camel case string with consecutive uppercase letters
    input_text = 'HTTPResponseCode'
    expected = 'http_response_code'
    assert camel_to_snake(input_text) == expected

def test_camel_to_snake_single_uppercase_letter_start():
    # Convert camel case string with single uppercase letter at the start
    input_text = 'Camel'
    expected = 'camel'
    assert camel_to_snake(input_text) == expected

def test_camel_to_snake_no_uppercase_letters():
    # Convert camel case string with no uppercase letters
    input_text = 'lowercase'
    expected = 'lowercase'
    assert camel_to_snake(input_text) == expected

def test_camel_to_snake_digits_and_uppercase_letters():
    # Convert camel case string with digits and uppercase letters
    input_text = 'Version2Number'
    expected = 'version2_number'
    assert camel_to_snake(input_text) == expected

def test_camel_to_snake_single_uppercase_letter_middle():
    # Convert camel case string with single uppercase letter in the middle
    input_text = 'SimpleXMLParser'
    expected = 'simple_xml_parser'
    assert camel_to_snake(input_text) == expected