def Sort(sub_li): 
    sub_li.sort(key = lambda x: x[1]) 
    return sub_li

import pytest

def test_sort_distinct_second_elements():
    sub_li = [[3, 2], [1, 5], [4, 1]]
    expected = [[4, 1], [3, 2], [1, 5]]
    assert Sort(sub_li) == expected

def test_sort_some_equal_second_elements():
    sub_li = [[10, 3], [5, 3], [7, 2]]
    expected = [[7, 2], [10, 3], [5, 3]]
    assert Sort(sub_li) == expected

def test_sort_empty_list():
    sub_li = []
    expected = []
    assert Sort(sub_li) == expected

def test_sort_single_element_list():
    sub_li = [[100, 50]]
    expected = [[100, 50]]
    assert Sort(sub_li) == expected

def test_sort_negative_and_positive_second_elements():
    sub_li = [[1, -1], [2, 0], [3, -5], [4, 3]]
    expected = [[3, -5], [1, -1], [2, 0], [4, 3]]
    assert Sort(sub_li) == expected