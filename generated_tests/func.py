def func(nums, k):
    import collections
    d = collections.defaultdict(int)
    for row in nums:
        for i in row:
            d[i] += 1
    temp = []
    import heapq
    for key, v in d.items():
        if len(temp) < k:
            temp.append((v, key))
            if len(temp) == k:
                heapq.heapify(temp)
        else:
            if v > temp[0][0]:
                heapq.heappop(temp)
                heapq.heappush(temp, (v, key))
    result = []
    while temp:
        v, key = heapq.heappop(temp)
        result.append(key)
    return result

import pytest

def test_top_2_most_frequent_multiple_duplicates():
    nums = [[1, 2, 2], [3, 1, 4], [2, 3, 3]]
    k = 2
    expected_output = [1, 2]
    assert func(nums, k) == expected_output

def test_top_3_most_frequent_k_equals_unique_elements():
    nums = [[5, 5, 6], [7, 6, 5], [7, 8, 8]]
    k = 3
    expected_output = [6, 7, 5]
    assert func(nums, k) == expected_output

def test_top_1_most_frequent_single_row():
    nums = [[10, 10, 10, 20, 20]]
    k = 1
    expected_output = [10]
    assert func(nums, k) == expected_output

def test_top_2_most_frequent_all_same_frequency():
    nums = [[1, 2], [3, 4]]
    k = 2
    expected_output = [1, 2]
    assert func(nums, k) == expected_output

def test_top_0_elements_edge_case():
    nums = [[1, 2, 3], [4, 5, 6]]
    k = 0
    expected_output = []
    assert func(nums, k) == expected_output