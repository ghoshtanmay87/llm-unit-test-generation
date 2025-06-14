import re
def split_upperstring(text):
 return (re.findall('[A-Z][^A-Z]*', text))

import pytest

def test_split_camel_case_multiple_uppercase_starts():
    # Scenario: Split a camel case string with multiple uppercase starts
    input_text = 'HelloWorld'
    expected = ['Hello', 'World']
    assert split_upperstring(input_text) == expected

def test_split_string_with_consecutive_uppercase_letters():
    # Scenario: Split a string with consecutive uppercase letters
    input_text = 'NASAResearch'
    expected = ['N', 'A', 'S', 'A', 'Research']
    assert split_upperstring(input_text) == expected

def test_split_string_single_uppercase_letter():
    # Scenario: Split a string with single uppercase letter
    input_text = 'A'
    expected = ['A']
    assert split_upperstring(input_text) == expected

def test_split_string_no_uppercase_letters():
    # Scenario: Split a string with no uppercase letters
    input_text = 'hello'
    expected = []
    assert split_upperstring(input_text) == expected

def test_split_string_starting_lowercase_followed_by_uppercase():
    # Scenario: Split a string starting with lowercase letter followed by uppercase
    input_text = 'helloWorld'
    expected = ['World']
    assert split_upperstring(input_text) == expected

def test_split_string_uppercase_letters_separated_by_lowercase():
    # Scenario: Split a string with uppercase letters separated by lowercase letters
    input_text = 'ThisIsATest'
    expected = ['This', 'Is', 'A', 'Test']
    assert split_upperstring(input_text) == expected

def test_split_string_all_uppercase_letters():
    # Scenario: Split a string with all uppercase letters
    input_text = 'USA'
    expected = ['U', 'S', 'A']
    assert split_upperstring(input_text) == expected