import heapq
def larg_nnum(list1,n):
 largest=heapq.nlargest(n,list1)
 return largest

import pytest

def test_larg_nnum_largest_3_distinct_positive():
    # Find the largest 3 numbers in a list of distinct positive integers
    input_list = [4, 1, 7, 3, 9, 2]
    n = 3
    expected = [9, 7, 4]
    assert larg_nnum(input_list, n) == expected

def test_larg_nnum_largest_2_with_duplicates():
    # Find the largest 2 numbers in a list with duplicates
    input_list = [5, 3, 5, 2, 5]
    n = 2
    expected = [5, 5]
    assert larg_nnum(input_list, n) == expected

def test_larg_nnum_largest_4_n_equals_list_length():
    # Find the largest 4 numbers when n equals the list length
    input_list = [10, 20, 30, 40]
    n = 4
    expected = [40, 30, 20, 10]
    assert larg_nnum(input_list, n) == expected

def test_larg_nnum_largest_1_with_neg_and_pos():
    # Find the largest 1 number in a list with negative and positive numbers
    input_list = [-10, 0, 5, -3, 2]
    n = 1
    expected = [5]
    assert larg_nnum(input_list, n) == expected

def test_larg_nnum_largest_0_non_empty_list():
    # Find the largest 0 numbers in a non-empty list
    input_list = [1, 2, 3, 4, 5]
    n = 0
    expected = []
    assert larg_nnum(input_list, n) == expected

def test_larg_nnum_largest_3_empty_list():
    # Find the largest 3 numbers in an empty list
    input_list = []
    n = 3
    expected = []
    assert larg_nnum(input_list, n) == expected