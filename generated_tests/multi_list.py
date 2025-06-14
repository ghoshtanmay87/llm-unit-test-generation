def multi_list(rownum,colnum):
  multi_list = [[0 for col in range(colnum)] for row in range(rownum)]
  for row in range(rownum):
    for col in range(colnum):
        multi_list[row][col]= row*col
  return multi_list

import pytest

def test_generate_3x3_multiplication_table():
    result = multi_list(rownum=3, colnum=3)
    expected = [[0, 0, 0], [0, 1, 2], [0, 2, 4]]
    assert result == expected

def test_generate_1x5_multiplication_table():
    result = multi_list(rownum=1, colnum=5)
    expected = [[0, 0, 0, 0, 0]]
    assert result == expected

def test_generate_4x1_multiplication_table():
    result = multi_list(rownum=4, colnum=1)
    expected = [[0], [0], [0], [0]]
    assert result == expected

def test_generate_0x0_multiplication_table_empty():
    result = multi_list(rownum=0, colnum=0)
    expected = []
    assert result == expected

def test_generate_2x4_multiplication_table():
    result = multi_list(rownum=2, colnum=4)
    expected = [[0, 0, 0, 0], [0, 1, 2, 3]]
    assert result == expected