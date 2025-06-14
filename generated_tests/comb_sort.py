def comb_sort(nums):
    shrink_fact = 1.3
    gaps = len(nums)
    swapped = True
    i = 0
    while gaps > 1 or swapped:
        gaps = int(float(gaps) / shrink_fact)
        swapped = False
        i = 0
        while gaps + i < len(nums):
            if nums[i] > nums[i+gaps]:
                nums[i], nums[i+gaps] = nums[i+gaps], nums[i]
                swapped = True
            i += 1
    return nums

import pytest

def test_comb_sort_already_sorted_list():
    # Sorting an already sorted list
    input_nums = [1, 2, 3, 4, 5]
    expected = [1, 2, 3, 4, 5]
    assert comb_sort(input_nums) == expected

def test_comb_sort_reverse_sorted_list():
    # Sorting a reverse sorted list
    input_nums = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    assert comb_sort(input_nums) == expected

def test_comb_sort_list_with_duplicates():
    # Sorting a list with duplicates
    input_nums = [3, 1, 2, 3, 1]
    expected = [1, 1, 2, 3, 3]
    assert comb_sort(input_nums) == expected

def test_comb_sort_single_element_list():
    # Sorting a single-element list
    input_nums = [42]
    expected = [42]
    assert comb_sort(input_nums) == expected

def test_comb_sort_empty_list():
    # Sorting an empty list
    input_nums = []
    expected = []
    assert comb_sort(input_nums) == expected

def test_comb_sort_negative_and_positive_numbers():
    # Sorting a list with negative and positive numbers
    input_nums = [0, -1, 5, -10, 3]
    expected = [-10, -1, 0, 3, 5]
    assert comb_sort(input_nums) == expected