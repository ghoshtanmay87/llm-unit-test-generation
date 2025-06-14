def rotate_right(list1,m,n):
  result =  list1[-(m):]+list1[:-(n)]
  return result

import pytest

def test_rotate_list_m2_n3_length5():
    # Rotate list with m=2 and n=3 on a list of length 5
    input_data = {'list1': [1, 2, 3, 4, 5], 'm': 2, 'n': 3}
    expected = [4, 5, 1, 2]
    assert rotate_right(**input_data) == expected

def test_rotate_list_m1_n1_length4():
    # Rotate list with m=1 and n=1 on a list of length 4
    input_data = {'list1': [10, 20, 30, 40], 'm': 1, 'n': 1}
    expected = [40, 10, 20, 30]
    assert rotate_right(**input_data) == expected

def test_rotate_list_m3_n2_length6():
    # Rotate list with m=3 and n=2 on a list of length 6
    input_data = {'list1': [5, 6, 7, 8, 9, 10], 'm': 3, 'n': 2}
    expected = [8, 9, 10, 5, 6, 7, 8]
    assert rotate_right(**input_data) == expected

def test_rotate_list_m0_n0_length3():
    # Rotate list with m=0 and n=0 on a list of length 3
    input_data = {'list1': [1, 2, 3], 'm': 0, 'n': 0}
    expected = [1, 2, 3]
    assert rotate_right(**input_data) == expected

def test_rotate_list_m4_n4_length4():
    # Rotate list with m=4 and n=4 on a list of length 4
    input_data = {'list1': [7, 8, 9, 10], 'm': 4, 'n': 4}
    expected = [7, 8, 9, 10]
    assert rotate_right(**input_data) == expected