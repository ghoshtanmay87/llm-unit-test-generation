def find_rect_num(n):
  return n*(n + 1)

import pytest

def test_find_rect_num_n_zero():
    # Calculate the number of rectangles for n=0
    result = find_rect_num(0)
    assert result == 0

def test_find_rect_num_n_one():
    # Calculate the number of rectangles for n=1
    result = find_rect_num(1)
    assert result == 2

def test_find_rect_num_n_two():
    # Calculate the number of rectangles for n=2
    result = find_rect_num(2)
    assert result == 6

def test_find_rect_num_n_five():
    # Calculate the number of rectangles for n=5
    result = find_rect_num(5)
    assert result == 30

def test_find_rect_num_n_ten():
    # Calculate the number of rectangles for n=10
    result = find_rect_num(10)
    assert result == 110