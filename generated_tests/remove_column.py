def remove_column(list1, n):
   for i in list1: 
    del i[n] 
   return list1

import pytest

def test_remove_first_column_from_2x3_matrix():
    input_data = [[1, 2, 3], [4, 5, 6]]
    n = 0
    expected = [[2, 3], [5, 6]]
    assert remove_column(input_data, n) == expected

def test_remove_second_column_from_3x3_matrix():
    input_data = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
    n = 1
    expected = [[10, 30], [40, 60], [70, 90]]
    assert remove_column(input_data, n) == expected

def test_remove_last_column_from_2x2_matrix():
    input_data = [[7, 8], [9, 10]]
    n = 1
    expected = [[7], [9]]
    assert remove_column(input_data, n) == expected

def test_remove_only_column_from_3x1_matrix():
    input_data = [[100], [200], [300]]
    n = 0
    expected = [[], [], []]
    assert remove_column(input_data, n) == expected

def test_remove_third_column_from_3x4_matrix():
    input_data = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    n = 2
    expected = [[1, 2, 4], [5, 6, 8], [9, 10, 12]]
    assert remove_column(input_data, n) == expected