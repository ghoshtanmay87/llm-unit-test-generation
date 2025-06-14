import heapq
def cheap_items(items,n):
  cheap_items = heapq.nsmallest(n, items, key=lambda s: s['price'])
  return cheap_items

import pytest

def test_find_2_cheapest_items_from_4_distinct_prices():
    items = [
        {'name': 'apple', 'price': 5.0},
        {'name': 'banana', 'price': 3.0},
        {'name': 'carrot', 'price': 4.0},
        {'name': 'date', 'price': 2.0}
    ]
    n = 2
    expected_output = [
        {'name': 'date', 'price': 2.0},
        {'name': 'banana', 'price': 3.0}
    ]
    assert cheap_items(items, n) == expected_output

def test_request_more_items_than_available():
    items = [
        {'name': 'apple', 'price': 5.0},
        {'name': 'banana', 'price': 3.0}
    ]
    n = 5
    expected_output = [
        {'name': 'banana', 'price': 3.0},
        {'name': 'apple', 'price': 5.0}
    ]
    assert cheap_items(items, n) == expected_output

def test_find_3_cheapest_items_with_duplicate_prices():
    items = [
        {'name': 'apple', 'price': 2.0},
        {'name': 'banana', 'price': 2.0},
        {'name': 'carrot', 'price': 3.0},
        {'name': 'date', 'price': 1.0}
    ]
    n = 3
    expected_output = [
        {'name': 'date', 'price': 1.0},
        {'name': 'apple', 'price': 2.0},
        {'name': 'banana', 'price': 2.0}
    ]
    assert cheap_items(items, n) == expected_output

def test_request_zero_items_from_non_empty_list():
    items = [
        {'name': 'apple', 'price': 1.0},
        {'name': 'banana', 'price': 2.0}
    ]
    n = 0
    expected_output = []
    assert cheap_items(items, n) == expected_output

def test_empty_items_list_with_non_zero_n():
    items = []
    n = 3
    expected_output = []
    assert cheap_items(items, n) == expected_output