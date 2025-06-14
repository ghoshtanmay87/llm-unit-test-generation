def shell_sort(my_list):
    gap = len(my_list) // 2
    while gap > 0:
        for i in range(gap, len(my_list)):
            current_item = my_list[i]
            j = i
            while j >= gap and my_list[j - gap] > current_item:
                my_list[j] = my_list[j - gap]
                j -= gap
            my_list[j] = current_item
        gap //= 2

    return my_list

import pytest

def test_sorting_empty_list_returns_empty_list():
    input_list = []
    expected = []
    assert shell_sort(input_list) == expected

def test_sorting_single_element_list_returns_same_list():
    input_list = [42]
    expected = [42]
    assert shell_sort(input_list) == expected

def test_sorting_two_elements_already_sorted():
    input_list = [1, 2]
    expected = [1, 2]
    assert shell_sort(input_list) == expected

def test_sorting_two_elements_descending_order():
    input_list = [2, 1]
    expected = [1, 2]
    assert shell_sort(input_list) == expected

def test_sorting_multiple_elements_random_order():
    input_list = [8, 5, 3, 7, 6, 2, 4, 1]
    expected = [1, 2, 3, 4, 5, 6, 7, 8]
    assert shell_sort(input_list) == expected

def test_sorting_list_with_repeated_elements():
    input_list = [4, 2, 4, 3, 2]
    expected = [2, 2, 3, 4, 4]
    assert shell_sort(input_list) == expected

def test_sorting_list_with_negative_and_positive_integers():
    input_list = [0, -1, 5, -3, 2]
    expected = [-3, -1, 0, 2, 5]
    assert shell_sort(input_list) == expected

def test_sorting_already_sorted_list():
    input_list = [1, 2, 3, 4, 5]
    expected = [1, 2, 3, 4, 5]
    assert shell_sort(input_list) == expected

def test_sorting_list_sorted_in_descending_order():
    input_list = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    assert shell_sort(input_list) == expected