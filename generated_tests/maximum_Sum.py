def maximum_Sum(list1): 
    maxi = -100000
    for x in list1: 
        sum = 0 
        for y in x: 
            sum+= y      
        maxi = max(sum,maxi)     
    return maxi

import pytest

def test_maximum_sum_positive_integers():
    # Find maximum sum among sublists with positive integers
    input_list = [[1, 2, 3], [4, 5], [6]]
    expected = 9
    assert maximum_Sum(input_list) == expected

def test_maximum_sum_negative_and_positive_integers():
    # Find maximum sum when sublists contain negative and positive integers
    input_list = [[-1, -2, -3], [4, -5], [6, -1]]
    expected = 5
    assert maximum_Sum(input_list) == expected

def test_maximum_sum_all_negative_sums():
    # Find maximum sum when all sublists have negative sums
    input_list = [[-10, -20], [-5, -15], [-1, -2, -3]]
    expected = -6
    assert maximum_Sum(input_list) == expected

def test_maximum_sum_with_empty_sublists():
    # Find maximum sum when list contains empty sublists
    input_list = [[], [1, 2], [3]]
    expected = 3
    assert maximum_Sum(input_list) == expected

def test_maximum_sum_single_sublist():
    # Find maximum sum when list contains a single sublist
    input_list = [[10, 20, 30]]
    expected = 60
    assert maximum_Sum(input_list) == expected

def test_maximum_sum_empty_list():
    # Find maximum sum when list is empty
    input_list = []
    expected = -100000
    assert maximum_Sum(input_list) == expected

def test_maximum_sum_sublists_with_zeros():
    # Find maximum sum when sublists contain zeros
    input_list = [[0, 0, 0], [0], [0, 0]]
    expected = 0
    assert maximum_Sum(input_list) == expected