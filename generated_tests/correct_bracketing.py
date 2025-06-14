def correct_bracketing(brackets: str):
    depth = 0
    for b in brackets:
        if b == '(':
            depth += 1
        else:
            depth -= 1
        if depth < 0:
            return False
    return depth == 0

import pytest

def test_empty_string_input_should_be_considered_correctly_bracketed():
    assert correct_bracketing('') is True

def test_single_pair_of_brackets_is_correctly_bracketed():
    assert correct_bracketing('()') is True

def test_nested_brackets_are_correctly_bracketed():
    assert correct_bracketing('(())') is True

def test_sequential_pairs_of_brackets_are_correctly_bracketed():
    assert correct_bracketing('()()') is True

def test_more_closing_brackets_than_opening_brackets_returns_false():
    assert correct_bracketing(')(') is False

def test_unbalanced_brackets_with_more_opening_brackets_returns_false():
    assert correct_bracketing('(()') is False

def test_unbalanced_brackets_with_closing_bracket_before_matching_opening_returns_false():
    assert correct_bracketing('())') is False

def test_long_balanced_nested_brackets_return_true():
    assert correct_bracketing('((()())())') is True

def test_long_unbalanced_brackets_with_early_closing_bracket_returns_false():
    assert correct_bracketing('(()))(') is False