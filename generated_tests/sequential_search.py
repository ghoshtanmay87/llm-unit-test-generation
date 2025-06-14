def sequential_search(dlist, item):
    pos = 0
    found = False
    while pos < len(dlist) and not found:
        if dlist[pos] == item:
            found = True
        else:
            pos = pos + 1
    return found, pos

import pytest

def test_item_present_at_beginning():
    dlist = [5, 3, 7, 1]
    item = 5
    expected = (True, 0)
    result = sequential_search(dlist, item)
    assert result == expected

def test_item_present_in_middle():
    dlist = [4, 8, 15, 16, 23, 42]
    item = 15
    expected = (True, 2)
    result = sequential_search(dlist, item)
    assert result == expected

def test_item_present_at_end():
    dlist = [10, 20, 30, 40, 50]
    item = 50
    expected = (True, 4)
    result = sequential_search(dlist, item)
    assert result == expected

def test_item_not_present():
    dlist = [1, 2, 3, 4, 5]
    item = 6
    expected = (False, 5)
    result = sequential_search(dlist, item)
    assert result == expected

def test_empty_list():
    dlist = []
    item = 1
    expected = (False, 0)
    result = sequential_search(dlist, item)
    assert result == expected

def test_multiple_occurrences_returns_first():
    dlist = [7, 8, 7, 9]
    item = 7
    expected = (True, 0)
    result = sequential_search(dlist, item)
    assert result == expected