def get_item(tup1,index):
  item = tup1[index]
  return item

import pytest

def test_retrieve_first_element_from_tuple_of_integers():
    tup1 = (10, 20, 30)
    index = 0
    expected = 10
    assert get_item(tup1, index) == expected

def test_retrieve_last_element_from_tuple_of_strings():
    tup1 = ('a', 'b', 'c')
    index = 2
    expected = 'c'
    assert get_item(tup1, index) == expected

def test_retrieve_middle_element_from_tuple_of_mixed_types():
    tup1 = (1, 'middle', 3.5)
    index = 1
    expected = 'middle'
    assert get_item(tup1, index) == expected

def test_retrieve_element_from_single_element_tuple():
    tup1 = (42,)
    index = 0
    expected = 42
    assert get_item(tup1, index) == expected

def test_retrieve_element_using_negative_index():
    tup1 = (100, 200, 300)
    index = -1
    expected = 300
    assert get_item(tup1, index) == expected