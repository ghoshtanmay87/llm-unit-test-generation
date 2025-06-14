def specified_element(nums, N):
    result = [i[N] for i in nums]
    return result

import pytest

def test_extract_element_index_0_from_each_sublist():
    nums = [[1, 2], [3, 4], [5, 6]]
    N = 0
    expected = [1, 3, 5]
    assert specified_element(nums, N) == expected

def test_extract_element_index_1_from_each_sublist():
    nums = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
    N = 1
    expected = [20, 50, 80]
    assert specified_element(nums, N) == expected

def test_extract_element_index_2_from_each_sublist_with_varying_lengths():
    nums = [[7, 8, 9], [1, 2, 3], [4, 5, 6]]
    N = 2
    expected = [9, 3, 6]
    assert specified_element(nums, N) == expected

def test_extract_element_index_0_from_single_element_sublists():
    nums = [[100], [200], [300]]
    N = 0
    expected = [100, 200, 300]
    assert specified_element(nums, N) == expected

def test_extract_element_index_1_from_sublists_with_two_elements():
    nums = [[-1, -2], [-3, -4], [-5, -6]]
    N = 1
    expected = [-2, -4, -6]
    assert specified_element(nums, N) == expected