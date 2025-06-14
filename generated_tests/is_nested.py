def is_nested(string):
    opening_bracket_index = []
    closing_bracket_index = []
    for i in range(len(string)):
        if string[i] == '[':
            opening_bracket_index.append(i)
        else:
            closing_bracket_index.append(i)
    closing_bracket_index.reverse()
    cnt = 0
    i = 0
    l = len(closing_bracket_index)
    for idx in opening_bracket_index:
        if i < l and idx < closing_bracket_index[i]:
            cnt += 1
            i += 1
    return cnt >= 2

import pytest

def test_string_with_two_properly_nested_brackets():
    # The string has two '[' at indices 0 and 1, and two ']' at indices 2 and 3.
    # The closing bracket indices reversed are [3, 2].
    # For opening index 0, 0 < 3 is True, count=1.
    # For opening index 1, 1 < 2 is True, count=2.
    # Since count >= 2, returns True.
    assert is_nested("[[]]") is True

def test_string_with_two_brackets_but_not_nested():
    # The string has '[' at indices 0 and 2, and ']' at indices 1 and 3.
    # Closing indices reversed: [3, 1].
    # For opening index 0, 0 < 3 True, count=1.
    # For opening index 2, 2 < 1 False, count remains 1.
    # Count is 1, less than 2, so returns False.
    assert is_nested("[][]") is False

def test_string_with_one_pair_of_brackets():
    # One '[' at index 0, one ']' at index 1.
    # Closing reversed: [1].
    # For opening index 0, 0 < 1 True, count=1.
    # Count is 1, less than 2, so returns False.
    assert is_nested("[]") is False

def test_string_with_no_brackets():
    # No '[' characters, so opening_bracket_index is empty.
    # Count remains 0, less than 2, returns False.
    assert is_nested("abc") is False

def test_string_with_three_nested_brackets():
    # Opening '[' at indices 0,1,2; closing ']' at indices 3,4,5.
    # Closing reversed: [5,4,3].
    # For idx=0, 0<5 True count=1;
    # idx=1, 1<4 True count=2;
    # idx=2, 2<3 True count=3.
    # Count=3 >=2 returns True.
    assert is_nested("[[[]]]") is True

def test_string_with_brackets_but_all_opening_after_closing():
    # Opening '[' at indices 2 and 3; closing ']' at indices 0 and 1.
    # Closing reversed: [1,0].
    # For idx=2, 2<1 False; idx=3, 3<0 False.
    # Count=0 <2 returns False.
    assert is_nested("][[]") is False