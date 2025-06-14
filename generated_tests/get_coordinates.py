def adjac(ele, sub = []): 
  if not ele: 
     yield sub 
  else: 
     yield from [idx for j in range(ele[0] - 1, ele[0] + 2) 
                for idx in adjac(ele[1:], sub + [j])] 
def get_coordinates(test_tup):
  res = list(adjac(test_tup))
  return (res)

import pytest

def test_generate_all_coordinate_combinations_2d_point_2_3():
    test_tup = [2, 3]
    expected_output = [[1, 2], [1, 3], [1, 4], [2, 2], [2, 3], [2, 4], [3, 2], [3, 3], [3, 4]]
    assert get_coordinates(test_tup) == expected_output

def test_generate_all_coordinate_combinations_1d_point_5():
    test_tup = [5]
    expected_output = [[4], [5], [6]]
    assert get_coordinates(test_tup) == expected_output

def test_generate_all_coordinate_combinations_3d_point_1_1_1():
    test_tup = [1, 1, 1]
    expected_output = [
        [0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [0, 1, 2], [0, 2, 0], [0, 2, 1], [0, 2, 2],
        [1, 0, 0], [1, 0, 1], [1, 0, 2], [1, 1, 0], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2],
        [2, 0, 0], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]
    ]
    assert get_coordinates(test_tup) == expected_output

def test_generate_all_coordinate_combinations_empty_input():
    test_tup = []
    expected_output = [[]]
    assert get_coordinates(test_tup) == expected_output

def test_generate_all_coordinate_combinations_2d_point_0_0():
    test_tup = [0, 0]
    expected_output = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 0], [0, 1], [1, -1], [1, 0], [1, 1]]
    assert get_coordinates(test_tup) == expected_output