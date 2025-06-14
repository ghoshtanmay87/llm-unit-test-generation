def min_length(list1):
   min_length = min(len(x) for x in  list1 )  
   min_list = min((x) for x in   list1)
   return(min_length, min_list)

import pytest

def test_min_length_varied_lengths_lex_smallest():
    # Find minimum length and lexicographically smallest list among multiple lists of varying lengths
    input_data = [[1, 2, 3], [4, 5], [6]]
    expected = (1, [6])
    assert min_length(input_data) == expected

def test_min_length_same_length_lex_smallest():
    # Find minimum length and lexicographically smallest list when all lists have the same length
    input_data = [[3, 4], [1, 2], [2, 3]]
    expected = (2, [1, 2])
    assert min_length(input_data) == expected

def test_min_length_contains_empty_list():
    # Find minimum length and lexicographically smallest list when lists contain empty list
    input_data = [[7, 8], [], [9]]
    expected = (0, [])
    assert min_length(input_data) == expected

def test_min_length_all_identical_lists():
    # Find minimum length and lexicographically smallest list when all lists are identical
    input_data = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]
    expected = (3, [5, 5, 5])
    assert min_length(input_data) == expected

def test_min_length_single_list_input():
    # Find minimum length and lexicographically smallest list with single list input
    input_data = [[10, 20, 30, 40]]
    expected = (4, [10, 20, 30, 40])
    assert min_length(input_data) == expected