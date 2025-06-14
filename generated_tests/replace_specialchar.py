import re
def replace_specialchar(text):
 return (re.sub("[ ,.]", ":", text))

import pytest

def test_replace_spaces_with_colons():
    input_text = 'hello world'
    expected = 'hello:world'
    assert replace_specialchar(input_text) == expected

def test_replace_commas_with_colons():
    input_text = 'apple,banana,orange'
    expected = 'apple:banana:orange'
    assert replace_specialchar(input_text) == expected

def test_replace_periods_with_colons():
    input_text = 'www.example.com'
    expected = 'www:example:com'
    assert replace_specialchar(input_text) == expected

def test_replace_multiple_special_characters_in_string():
    input_text = 'a, b. c'
    expected = 'a::b::c'
    assert replace_specialchar(input_text) == expected

def test_string_with_no_special_characters_remains_unchanged():
    input_text = 'hello_world'
    expected = 'hello_world'
    assert replace_specialchar(input_text) == expected

def test_empty_string_input_returns_empty_string():
    input_text = ''
    expected = ''
    assert replace_specialchar(input_text) == expected

def test_string_with_consecutive_special_characters():
    input_text = 'a,, b.. c'
    expected = 'a::::b::::c'
    assert replace_specialchar(input_text) == expected