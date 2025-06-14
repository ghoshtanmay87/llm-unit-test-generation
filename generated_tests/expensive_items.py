import heapq
def expensive_items(items,n):
  expensive_items = heapq.nlargest(n, items, key=lambda s: s['price'])
  return expensive_items

import pytest

def test_top_2_most_expensive_items_distinct_prices():
    items = [
        {'name': 'apple', 'price': 1.0},
        {'name': 'banana', 'price': 0.5},
        {'name': 'cherry', 'price': 2.0},
        {'name': 'date', 'price': 1.5}
    ]
    n = 2
    expected_output = [
        {'name': 'cherry', 'price': 2.0},
        {'name': 'date', 'price': 1.5}
    ]
    assert expensive_items(items, n) == expected_output

def test_top_3_most_expensive_items_n_equals_number_of_items():
    items = [
        {'name': 'pen', 'price': 1.2},
        {'name': 'notebook', 'price': 3.5},
        {'name': 'eraser', 'price': 0.8}
    ]
    n = 3
    expected_output = [
        {'name': 'notebook', 'price': 3.5},
        {'name': 'pen', 'price': 1.2},
        {'name': 'eraser', 'price': 0.8}
    ]
    assert expensive_items(items, n) == expected_output

def test_top_1_most_expensive_item_multiple_items():
    items = [
        {'name': 'chair', 'price': 45.0},
        {'name': 'table', 'price': 150.0},
        {'name': 'lamp', 'price': 30.0}
    ]
    n = 1
    expected_output = [
        {'name': 'table', 'price': 150.0}
    ]
    assert expensive_items(items, n) == expected_output

def test_top_0_most_expensive_items_returns_empty_list():
    items = [
        {'name': 'item1', 'price': 10.0},
        {'name': 'item2', 'price': 20.0}
    ]
    n = 0
    expected_output = []
    assert expensive_items(items, n) == expected_output

def test_top_2_most_expensive_items_with_same_price():
    items = [
        {'name': 'itemA', 'price': 100.0},
        {'name': 'itemB', 'price': 100.0},
        {'name': 'itemC', 'price': 50.0}
    ]
    n = 2
    expected_output = [
        {'name': 'itemA', 'price': 100.0},
        {'name': 'itemB', 'price': 100.0}
    ]
    assert expensive_items(items, n) == expected_output