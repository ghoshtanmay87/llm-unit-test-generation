def cycpattern_check(a, b):
    l = len(b)
    pat = b + b
    for i in range(len(a) - l + 1):
        for j in range(l + 1):
            if a[i:i + l] == pat[j:j + l]:
                return True
    return False

import pytest

def test_cycpattern_check_exact_equality():
    a = [1, 2, 3]
    b = [1, 2, 3]
    expected = True
    assert cycpattern_check(a, b) == expected

def test_cycpattern_check_rotation_of_b():
    a = [2, 3, 1]
    b = [1, 2, 3]
    expected = True
    assert cycpattern_check(a, b) == expected

def test_cycpattern_check_not_a_rotation():
    a = [3, 2, 1]
    b = [1, 2, 3]
    expected = False
    assert cycpattern_check(a, b) == expected

def test_cycpattern_check_a_longer_contains_rotation():
    a = [0, 2, 3, 1, 4]
    b = [1, 2, 3]
    expected = True
    assert cycpattern_check(a, b) == expected

def test_cycpattern_check_a_shorter_than_b():
    a = [1, 2]
    b = [1, 2, 3]
    expected = False
    assert cycpattern_check(a, b) == expected

def test_cycpattern_check_both_empty_lists():
    a = []
    b = []
    expected = True
    assert cycpattern_check(a, b) == expected

def test_cycpattern_check_b_empty_a_nonempty():
    a = [1, 2, 3]
    b = []
    expected = True
    assert cycpattern_check(a, b) == expected

def test_cycpattern_check_multiple_rotations_in_a():
    a = [3, 1, 2, 3, 1, 2]
    b = [1, 2, 3]
    expected = True
    assert cycpattern_check(a, b) == expected