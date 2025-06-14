def count_integer(list1):
    ctr = 0
    for i in list1:
        if isinstance(i, int):
            ctr = ctr + 1
    return ctr

import pytest

def test_count_integers_mixed_types():
    # The list contains integers 1, 2, and 4. Other elements are string or float, so only 3 integers are counted.
    input_list = [1, 'a', 3.5, 2, '3', 4]
    expected = 3
    assert count_integer(input_list) == expected

def test_count_integers_only_integers():
    # All elements are integers, so the count is 4.
    input_list = [10, 20, 30, 40]
    expected = 4
    assert count_integer(input_list) == expected

def test_count_integers_no_integers_but_bool_present():
    # True is a bool, which is a subclass of int, so it counts as an int.
    # Therefore, the count is 1.
    input_list = ['one', 2.0, None, True, 3.5]
    expected = 1
    assert count_integer(input_list) == expected

def test_count_integers_with_boolean_values():
    # bool is a subclass of int, so all four elements are counted as integers.
    input_list = [True, False, 1, 0]
    expected = 4
    assert count_integer(input_list) == expected

def test_count_integers_empty_list():
    # The list is empty, so no integers are present.
    input_list = []
    expected = 0
    assert count_integer(input_list) == expected

def test_count_integers_negative_and_zero():
    # The integers are -1, 0, and -5. The float 3.14 and string '0' are not integers.
    input_list = [-1, 0, -5, 3.14, '0']
    expected = 3
    assert count_integer(input_list) == expected