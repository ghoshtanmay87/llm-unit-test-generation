def exchange(lst1, lst2):
    odd = 0
    even = 0
    for i in lst1:
        if i % 2 == 1:
            odd += 1
    for i in lst2:
        if i % 2 == 0:
            even += 1
    if even >= odd:
        return 'YES'
    return 'NO'

import pytest

def test_more_or_equal_even_in_lst2_than_odd_in_lst1():
    lst1 = [1, 2, 3]
    lst2 = [2, 4, 6]
    expected = 'YES'
    assert exchange(lst1, lst2) == expected

def test_fewer_even_in_lst2_than_odd_in_lst1():
    lst1 = [1, 3, 5]
    lst2 = [2, 3, 5]
    expected = 'NO'
    assert exchange(lst1, lst2) == expected

def test_equal_odd_in_lst1_and_even_in_lst2():
    lst1 = [1, 3, 4]
    lst2 = [2, 5, 6]
    expected = 'YES'
    assert exchange(lst1, lst2) == expected

def test_no_odd_in_lst1_some_even_in_lst2():
    lst1 = [2, 4, 6]
    lst2 = [1, 2, 3]
    expected = 'YES'
    assert exchange(lst1, lst2) == expected

def test_no_even_in_lst2_some_odd_in_lst1():
    lst1 = [1, 3, 5]
    lst2 = [1, 3, 5]
    expected = 'NO'
    assert exchange(lst1, lst2) == expected

def test_empty_lists_for_both():
    lst1 = []
    lst2 = []
    expected = 'YES'
    assert exchange(lst1, lst2) == expected

def test_odd_in_lst1_no_even_in_lst2_but_odd_in_lst2():
    lst1 = [7, 9]
    lst2 = [1, 3, 5]
    expected = 'NO'
    assert exchange(lst1, lst2) == expected

def test_no_odd_in_lst1_no_even_in_lst2():
    lst1 = [2, 4, 6]
    lst2 = [1, 3, 5]
    expected = 'YES'
    assert exchange(lst1, lst2) == expected