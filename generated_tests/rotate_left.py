def rotate_left(list1,m,n):
  result =  list1[m:]+list1[:n]
  return result

import pytest

def test_rotate_left_m0_n0_integers():
    # Rotate left with m=0 and n=0 on a list of integers
    input_list = [1, 2, 3, 4, 5]
    m = 0
    n = 0
    expected = [1, 2, 3, 4, 5]
    assert rotate_left(input_list, m, n) == expected

def test_rotate_left_m2_n2_integers():
    # Rotate left with m=2 and n=2 on a list of integers
    input_list = [1, 2, 3, 4, 5]
    m = 2
    n = 2
    expected = [3, 4, 5, 1, 2]
    assert rotate_left(input_list, m, n) == expected

def test_rotate_left_m3_n3_integers():
    # Rotate left with m=3 and n=3 on a list of integers
    input_list = [10, 20, 30, 40, 50]
    m = 3
    n = 3
    expected = [40, 50, 10, 20, 30]
    assert rotate_left(input_list, m, n) == expected

def test_rotate_left_m1_n1_strings():
    # Rotate left with m=1 and n=1 on a list of strings
    input_list = ['a', 'b', 'c', 'd']
    m = 1
    n = 1
    expected = ['b', 'c', 'd', 'a']
    assert rotate_left(input_list, m, n) == expected

def test_rotate_left_m0_n3_integers():
    # Rotate left with m=0 and n=3 on a list of integers
    input_list = [7, 8, 9, 10]
    m = 0
    n = 3
    expected = [7, 8, 9, 10, 7, 8, 9]
    assert rotate_left(input_list, m, n) == expected