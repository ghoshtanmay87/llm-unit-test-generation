def extract_index_list(l1, l2, l3):
    result = []
    for m, n, o in zip(l1, l2, l3):
        if (m == n == o):
            result.append(m)
    return result

import pytest

def test_all_three_lists_identical_elements():
    l1 = [1, 2, 3]
    l2 = [1, 2, 3]
    l3 = [1, 2, 3]
    expected = [1, 2, 3]
    assert extract_index_list(l1, l2, l3) == expected

def test_no_elements_match_across_all_three_lists():
    l1 = [1, 2, 3]
    l2 = [4, 5, 6]
    l3 = [7, 8, 9]
    expected = []
    assert extract_index_list(l1, l2, l3) == expected

def test_some_elements_match_across_all_three_lists():
    l1 = [1, 2, 3, 4]
    l2 = [1, 5, 3, 8]
    l3 = [1, 7, 3, 4]
    expected = [1, 3]
    assert extract_index_list(l1, l2, l3) == expected

def test_lists_contain_strings_with_some_matching_elements():
    l1 = ['a', 'b', 'c']
    l2 = ['a', 'x', 'c']
    l3 = ['a', 'b', 'c']
    expected = ['a', 'c']
    assert extract_index_list(l1, l2, l3) == expected

def test_lists_of_different_lengths_process_up_to_shortest_length():
    l1 = [1, 2, 3, 4]
    l2 = [1, 2, 0]
    l3 = [1, 2, 3, 4, 5]
    expected = [1, 2]
    assert extract_index_list(l1, l2, l3) == expected