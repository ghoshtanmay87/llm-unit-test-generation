from heapq import heappop, heappush
class Node:
    def __init__(self, value, list_num, index):
        self.value = value
        self.list_num = list_num
        self.index = index
    def __lt__(self, other):
        return self.value < other.value
def find_minimum_range(list):
    high = float('-inf')
    p = (0, float('inf'))
    pq = []
    for i in range(len(list)):
        heappush(pq, Node(list[i][0], i, 0))
        high = max(high, list[i][0])
    while True:
        top = heappop(pq)
        low = top.value
        i = top.list_num
        j = top.index
        if high - low < p[1] - p[0]:
            p = (low, high)
        if j == len(list[i]) - 1:
            return p
        heappush(pq, Node(list[i][j + 1], i, j + 1))
        high = max(high, list[i][j + 1])

import pytest

def test_minimum_range_single_element_lists():
    # Each list has one element: 1, 2, and 3.
    # The only possible range covering all is from 1 to 3.
    input_lists = [[1], [2], [3]]
    expected = (1, 3)
    assert find_minimum_range(input_lists) == expected

def test_minimum_range_all_lists_overlapping_elements():
    # Lists have overlapping elements.
    # The smallest range covering all lists is (4, 5).
    input_lists = [[4, 10, 15], [0, 9, 12], [5, 18, 22]]
    expected = (4, 5)
    assert find_minimum_range(input_lists) == expected

def test_minimum_range_lists_with_identical_elements():
    # All lists start with 1, so the smallest range is (1, 1).
    input_lists = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
    expected = (1, 1)
    assert find_minimum_range(input_lists) == expected

def test_minimum_range_one_list_larger_values():
    # The smallest range found is (4, 7).
    input_lists = [[1, 5, 8], [4, 12], [7, 8, 10]]
    expected = (4, 7)
    assert find_minimum_range(input_lists) == expected

def test_minimum_range_lists_varying_lengths():
    # The smallest range found is (9, 12).
    input_lists = [[1, 9], [4, 10, 15], [7, 12]]
    expected = (9, 12)
    assert find_minimum_range(input_lists) == expected