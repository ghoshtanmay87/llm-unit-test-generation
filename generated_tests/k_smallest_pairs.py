import heapq
def k_smallest_pairs(nums1, nums2, k):
   queue = []
   def push(i, j):
       if i < len(nums1) and j < len(nums2):
           heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
   push(0, 0)
   pairs = []
   while queue and len(pairs) < k:
       _, i, j = heapq.heappop(queue)
       pairs.append([nums1[i], nums2[j]])
       push(i, j + 1)
       if j == 0:
           push(i + 1, 0)
   return pairs

import pytest

def test_find_3_smallest_pairs_from_two_sorted_arrays_with_multiple_elements():
    nums1 = [1, 7, 11]
    nums2 = [2, 4, 6]
    k = 3
    expected_output = [[1, 2], [1, 4], [1, 6]]
    assert k_smallest_pairs(nums1, nums2, k) == expected_output

def test_find_3_smallest_pairs_when_k_larger_than_total_possible_pairs():
    nums1 = [1, 1, 2]
    nums2 = [1, 2, 3]
    k = 10
    expected_output = [[1, 1], [1, 1], [1, 2], [1, 2], [2, 1], [1, 3], [1, 3], [2, 2], [2, 3]]
    assert k_smallest_pairs(nums1, nums2, k) == expected_output

def test_find_2_smallest_pairs_when_one_array_is_empty():
    nums1 = []
    nums2 = [1, 2, 3]
    k = 2
    expected_output = []
    assert k_smallest_pairs(nums1, nums2, k) == expected_output

def test_find_1_smallest_pair_when_both_arrays_have_one_element():
    nums1 = [1]
    nums2 = [2]
    k = 1
    expected_output = [[1, 2]]
    assert k_smallest_pairs(nums1, nums2, k) == expected_output

def test_find_4_smallest_pairs_with_arrays_having_duplicates():
    nums1 = [1, 1, 2]
    nums2 = [1, 2]
    k = 4
    expected_output = [[1, 1], [1, 1], [1, 2], [1, 2]]
    assert k_smallest_pairs(nums1, nums2, k) == expected_output

def test_find_5_smallest_pairs_when_k_is_zero():
    nums1 = [1, 2]
    nums2 = [3, 4]
    k = 0
    expected_output = []
    assert k_smallest_pairs(nums1, nums2, k) == expected_output