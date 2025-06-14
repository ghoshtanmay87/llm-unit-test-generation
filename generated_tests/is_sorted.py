def is_sorted(lst):
    count_digit = dict([(i, 0) for i in lst])
    for i in lst:
        count_digit[i] += 1
    if any((count_digit[i] > 2 for i in lst)):
        return False
    if all((lst[i - 1] <= lst[i] for i in range(1, len(lst)))):
        return True
    else:
        return False

import pytest

def test_list_all_unique_elements_ascending():
    # List with all unique elements in ascending order
    lst = [1, 2, 3, 4, 5]
    expected = True
    assert is_sorted(lst) == expected

def test_list_element_appearing_more_than_twice():
    # List with an element appearing more than twice
    lst = [1, 2, 2, 2, 3]
    expected = False
    assert is_sorted(lst) == expected

def test_list_elements_at_most_twice_not_sorted():
    # List with elements appearing at most twice but not sorted
    lst = [1, 3, 2, 4]
    expected = False
    assert is_sorted(lst) == expected

def test_list_elements_exactly_twice_sorted():
    # List with elements appearing exactly twice and sorted
    lst = [1, 1, 2, 2, 3, 3]
    expected = True
    assert is_sorted(lst) == expected

def test_empty_list():
    # Empty list
    lst = []
    expected = True
    assert is_sorted(lst) == expected

def test_list_one_element_twice_not_sorted():
    # List with one element repeated twice but not sorted
    lst = [2, 1]
    expected = False
    assert is_sorted(lst) == expected

def test_list_one_element_twice_sorted():
    # List with one element repeated twice and sorted
    lst = [1, 1]
    expected = True
    assert is_sorted(lst) == expected

def test_list_multiple_elements_some_twice_sorted():
    # List with multiple elements, some repeated twice, sorted
    lst = [1, 2, 2, 3, 4, 4, 5]
    expected = True
    assert is_sorted(lst) == expected

def test_list_multiple_elements_some_twice_not_sorted():
    # List with multiple elements, some repeated twice, not sorted
    lst = [1, 2, 4, 3, 4, 5]
    expected = False
    assert is_sorted(lst) == expected