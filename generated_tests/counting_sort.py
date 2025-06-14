def counting_sort(my_list):
    max_value = 0
    for i in range(len(my_list)):
        if my_list[i] > max_value:
            max_value = my_list[i]
    buckets = [0] * (max_value + 1)
    for i in my_list:
        buckets[i] += 1
    i = 0
    for j in range(max_value + 1):
         for a in range(buckets[j]):
             my_list[i] = j
             i += 1
    return my_list

import pytest

def test_sorting_list_with_distinct_positive_integers():
    input_list = [3, 1, 4, 2]
    expected = [1, 2, 3, 4]
    assert counting_sort(input_list) == expected

def test_sorting_list_with_repeated_elements():
    input_list = [2, 3, 2, 1, 3]
    expected = [1, 2, 2, 3, 3]
    assert counting_sort(input_list) == expected

def test_sorting_list_with_all_elements_the_same():
    input_list = [5, 5, 5, 5]
    expected = [5, 5, 5, 5]
    assert counting_sort(input_list) == expected

def test_sorting_list_with_single_element():
    input_list = [7]
    expected = [7]
    assert counting_sort(input_list) == expected

def test_sorting_list_with_zero_included():
    input_list = [0, 2, 1, 0]
    expected = [0, 0, 1, 2]
    assert counting_sort(input_list) == expected

def test_sorting_empty_list():
    input_list = []
    expected = []
    assert counting_sort(input_list) == expected

def test_sorting_list_with_elements_less_than_initial_max_value_zero():
    input_list = [0, 0, 0]
    expected = [0, 0, 0]
    assert counting_sort(input_list) == expected