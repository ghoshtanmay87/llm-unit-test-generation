from collections import deque
def check_expression(exp):
    if len(exp) & 1:
        return False
    stack = deque()
    for ch in exp:
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        if ch == ')' or ch == '}' or ch == ']':
            if not stack:
                return False
            top = stack.pop()
            if (top == '(' and ch != ')') or (top == '{' and ch != '}' or (top == '[' and ch != ']')):
                return False
    return not stack

import pytest

def test_expression_with_odd_length_returns_false_immediately_case1():
    # Scenario: Expression with odd length returns False immediately
    exp = "(]"
    expected = False
    assert check_expression(exp) == expected

def test_expression_with_odd_length_returns_false_immediately_case2():
    # Scenario: Expression with odd length returns False immediately
    exp = "("
    expected = False
    assert check_expression(exp) == expected

def test_correctly_matched_simple_parentheses():
    # Scenario: Correctly matched simple parentheses
    exp = "()"
    expected = True
    assert check_expression(exp) == expected

def test_correctly_matched_nested_brackets():
    # Scenario: Correctly matched nested brackets
    exp = "({[]})"
    expected = True
    assert check_expression(exp) == expected

def test_mismatched_brackets_returns_false():
    # Scenario: Mismatched brackets returns False
    exp = "([)]"
    expected = False
    assert check_expression(exp) == expected

def test_unmatched_closing_bracket_returns_false():
    # Scenario: Unmatched closing bracket returns False
    exp = "]"
    expected = False
    assert check_expression(exp) == expected

def test_empty_string_returns_true():
    # Scenario: Empty string returns True
    exp = ""
    expected = True
    assert check_expression(exp) == expected

def test_expression_with_only_opening_brackets_returns_false():
    # Scenario: Expression with only opening brackets returns False
    exp = "((("
    expected = False
    assert check_expression(exp) == expected

def test_expression_with_balanced_brackets_but_extra_opening_bracket_returns_false():
    # Scenario: Expression with balanced brackets but extra opening bracket returns False
    exp = "(()"
    expected = False
    assert check_expression(exp) == expected

def test_expression_with_balanced_brackets_but_extra_closing_bracket_returns_false():
    # Scenario: Expression with balanced brackets but extra closing bracket returns False
    exp = "())"
    expected = False
    assert check_expression(exp) == expected

def test_expression_with_multiple_pairs_of_balanced_brackets():
    # Scenario: Expression with multiple pairs of balanced brackets
    exp = "()[]{}"
    expected = True
    assert check_expression(exp) == expected

def test_expression_with_incorrect_bracket_order_returns_false():
    # Scenario: Expression with incorrect bracket order returns False
    exp = "}{"
    expected = False
    assert check_expression(exp) == expected