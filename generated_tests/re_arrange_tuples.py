def re_arrange_tuples(test_list, ord_list):
  temp = dict(test_list)
  res = [(key, temp[key]) for key in ord_list]
  return (res)

import pytest

def test_rearranging_tuples_with_matching_keys_in_order_list():
    test_list = [('a', 1), ('b', 2), ('c', 3)]
    ord_list = ['b', 'c', 'a']
    expected_output = [('b', 2), ('c', 3), ('a', 1)]
    assert re_arrange_tuples(test_list, ord_list) == expected_output

def test_rearranging_tuples_with_ord_list_as_subset_of_keys():
    test_list = [('x', 10), ('y', 20), ('z', 30)]
    ord_list = ['z', 'x']
    expected_output = [('z', 30), ('x', 10)]
    assert re_arrange_tuples(test_list, ord_list) == expected_output

def test_rearranging_tuples_with_ord_list_having_keys_not_in_test_list():
    test_list = [('p', 5), ('q', 6)]
    ord_list = ['q', 'r']
    expected_output = [('q', 6)]
    assert re_arrange_tuples(test_list, ord_list) == expected_output

def test_empty_test_list_and_non_empty_ord_list():
    test_list = []
    ord_list = ['a', 'b']
    expected_output = []
    assert re_arrange_tuples(test_list, ord_list) == expected_output

def test_non_empty_test_list_and_empty_ord_list():
    test_list = [('a', 1), ('b', 2)]
    ord_list = []
    expected_output = []
    assert re_arrange_tuples(test_list, ord_list) == expected_output

def test_test_list_with_duplicate_keys_last_occurrence_used():
    test_list = [('a', 1), ('b', 2), ('a', 3)]
    ord_list = ['a', 'b']
    expected_output = [('a', 3), ('b', 2)]
    assert re_arrange_tuples(test_list, ord_list) == expected_output