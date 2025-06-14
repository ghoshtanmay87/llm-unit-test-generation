def strange_sort_list(lst):
    res, switch = ([], True)
    while lst:
        res.append(min(lst) if switch else max(lst))
        lst.remove(res[-1])
        switch = not switch
    return res

import pytest

def test_sort_empty_list():
    # The input list is empty, so the while loop never runs and the function returns an empty list.
    input_lst = []
    expected = []
    assert strange_sort_list(input_lst) == expected

def test_sort_list_with_one_element():
    # With one element, the function appends the min (which is 5), removes it, and ends, returning [5].
    input_lst = [5]
    expected = [5]
    assert strange_sort_list(input_lst) == expected

def test_sort_list_with_two_elements():
    # First append min(3,7)=3, remove 3; then append max(7)=7, remove 7; result is [3, 7].
    input_lst = [3, 7]
    expected = [3, 7]
    assert strange_sort_list(input_lst) == expected

def test_sort_list_with_three_elements():
    # Append min(1,4,9)=1, remove 1; append max(4,9)=9, remove 9; append min(4)=4, remove 4; result is [1, 9, 4].
    input_lst = [1, 4, 9]
    expected = [1, 9, 4]
    assert strange_sort_list(input_lst) == expected

def test_sort_list_with_repeated_elements():
    # Append min(1,2,2,3)=1, remove 1; append max(2,2,3)=3, remove 3; append min(2,2)=2, remove one 2; append max(2)=2, remove 2; result is [1, 3, 2, 2].
    input_lst = [1, 2, 2, 3]
    expected = [1, 3, 2, 2]
    assert strange_sort_list(input_lst) == expected

def test_sort_list_with_all_identical_elements():
    # Min and max are always 5; the function removes one 5 each iteration, resulting in [5, 5, 5].
    input_lst = [5, 5, 5]
    expected = [5, 5, 5]
    assert strange_sort_list(input_lst) == expected

def test_sort_list_with_negative_and_positive_numbers():
    # Append min(-103, -5, -1, 0, 3) = -103, remove -103; append max(-5, -1, 0, 3) = 3, remove 3; append min(-5, -1, 0) = -5, remove -5; append max(-1, 0) = 0, remove 0; append min(-1) = -1, remove -1; result is [-103, 3, -5, 0, -1].
    input_lst = [-5, 3, -1, 0, -103]
    expected = [-103, 3, -5, 0, -1]
    assert strange_sort_list(input_lst) == expected

def test_sort_list_already_sorted_ascending():
    # Append min(1,2,3,4,5)=1, remove 1; append max(2,3,4,5)=5, remove 5; append min(2,3,4)=2, remove 2; append max(3,4)=4, remove 4; append min(3)=3, remove 3; result is [1, 5, 2, 4, 3].
    input_lst = [1, 2, 3, 4, 5]
    expected = [1, 5, 2, 4, 3]
    assert strange_sort_list(input_lst) == expected

def test_sort_list_already_sorted_descending():
    # Append min(5,4,3,2,1)=1, remove 1; append max(5,4,3,2)=5, remove 5; append min(4,3,2)=2, remove 2; append max(4,3)=4, remove 4; append min(3)=3, remove 3; result is [1, 5, 2, 4, 3].
    input_lst = [5, 4, 3, 2, 1]
    expected = [1, 5, 2, 4, 3]
    assert strange_sort_list(input_lst) == expected