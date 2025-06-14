from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:

    def parse_paren_group(s):
        depth = 0
        max_depth = 0
        for c in s:
            if c == '(':
                depth += 1
                max_depth = max(depth, max_depth)
            else:
                depth -= 1
        return max_depth
    return [parse_paren_group(x) for x in paren_string.split(' ') if x]

import pytest

def test_single_group_one_pair_of_parentheses():
    input_data = {'paren_string': '(())'}
    expected = [2]
    assert parse_nested_parens(**input_data) == expected

def test_multiple_groups_separated_by_spaces_varying_depths():
    input_data = {'paren_string': '() (()) ((()))'}
    expected = [1, 2, 3]
    assert parse_nested_parens(**input_data) == expected

def test_empty_input_string():
    input_data = {'paren_string': ''}
    expected = []
    assert parse_nested_parens(**input_data) == expected

def test_input_with_multiple_spaces_between_groups():
    input_data = {'paren_string': '(())  ()   ((()))'}
    expected = [2, 1, 3]
    assert parse_nested_parens(**input_data) == expected

def test_single_group_no_nesting():
    input_data = {'paren_string': '()'}
    expected = [1]
    assert parse_nested_parens(**input_data) == expected

def test_multiple_groups_single_parentheses_each():
    input_data = {'paren_string': '() () ()'}
    expected = [1, 1, 1]
    assert parse_nested_parens(**input_data) == expected

def test_group_with_deep_nesting_and_multiple_groups():
    input_data = {'paren_string': '((())) (()()) ((()()))'}
    expected = [3, 2, 3]
    assert parse_nested_parens(**input_data) == expected