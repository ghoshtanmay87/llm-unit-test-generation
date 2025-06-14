def decode_list(alist):
    def aux(g):
        if isinstance(g, list):
            return [(g[1], range(g[0]))]
        else:
            return [(g, [0])]
    return [x for g in alist for x, R in aux(g) for i in R]

import pytest

def test_decode_list_only_integers():
    alist = [5, 3]
    expected_output = [5, 3]
    assert decode_list(alist) == expected_output

def test_decode_list_only_lists_of_two_elements():
    alist = [[3, 2], [2, 4]]
    expected_output = [2, 2, 2, 4, 4]
    assert decode_list(alist) == expected_output

def test_decode_list_mixed_integers_and_lists():
    alist = [4, [2, 7], 9]
    expected_output = [4, 7, 7, 9]
    assert decode_list(alist) == expected_output

def test_decode_list_list_with_zero_count():
    alist = [[0, 10], 5]
    expected_output = [5]
    assert decode_list(alist) == expected_output

def test_decode_list_list_with_count_one():
    alist = [[1, 8], 2]
    expected_output = [8, 2]
    assert decode_list(alist) == expected_output