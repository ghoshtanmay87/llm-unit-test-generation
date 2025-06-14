import re
def remove_parenthesis(items):
 for item in items:
    return (re.sub(r" ?\([^)]+\)", "", item))

import pytest

def test_remove_single_parenthesis_group_with_leading_space():
    # Remove a single parenthesis group with leading space
    result = remove_parenthesis(['apple (fruit)'])
    assert result == 'apple'

def test_remove_parenthesis_group_without_leading_space():
    # Remove parenthesis group without leading space
    result = remove_parenthesis(['banana(fruit)'])
    assert result == 'banana'

def test_remove_only_first_item_parenthesis_group_in_list():
    # Remove only the first item parenthesis group in list
    result = remove_parenthesis(['car (vehicle)', 'bike (two wheels)'])
    assert result == 'car'

def test_no_parenthesis_in_string():
    # No parenthesis in string
    result = remove_parenthesis(['orange'])
    assert result == 'orange'

def test_parentheses_with_multiple_words_inside():
    # Parentheses with multiple words inside
    result = remove_parenthesis(['grape (purple fruit)'])
    assert result == 'grape'

def test_parentheses_with_no_leading_space():
    # Parentheses with no leading space
    result = remove_parenthesis(['melon(fruit)'])
    assert result == 'melon'

def test_parentheses_with_nested_parentheses_inside_not_handled():
    # Parentheses with nested parentheses inside (not handled)
    result = remove_parenthesis(['test (example (nested))'])
    assert result == 'test (example (nested))'