def match_parens(lst):

    def check(s):
        val = 0
        for i in s:
            if i == '(':
                val = val + 1
            else:
                val = val - 1
            if val < 0:
                return False
        return True if val == 0 else False
    S1 = lst[0] + lst[1]
    S2 = lst[1] + lst[0]
    return 'Yes' if check(S1) or check(S2) else 'No'

import pytest

def test_balanced_parentheses_concatenated_in_either_order():
    """Test balanced parentheses when concatenated in either order."""
    input_data = {'lst': ['(', ')']}
    expected_output = 'Yes'
    assert match_parens(**input_data) == expected_output

def test_unbalanced_parentheses_concatenated_in_both_orders():
    """Test unbalanced parentheses when concatenated in both orders."""
    input_data = {'lst': ['(', '(']}
    expected_output = 'No'
    assert match_parens(**input_data) == expected_output

def test_one_balanced_string_and_one_empty_string():
    """Test one balanced string and one empty string."""
    input_data = {'lst': ['()', '']}
    expected_output = 'Yes'
    assert match_parens(**input_data) == expected_output

def test_unbalanced_parentheses_with_non_matching_counts():
    """Test unbalanced parentheses with non-matching counts."""
    input_data = {'lst': ['(()', ')']}
    expected_output = 'No'
    assert match_parens(**input_data) == expected_output

def test_two_empty_strings():
    """Test two empty strings."""
    input_data = {'lst': ['', '']}
    expected_output = 'Yes'
    assert match_parens(**input_data) == expected_output