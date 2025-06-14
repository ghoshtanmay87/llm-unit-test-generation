def tri(n):
    if n == 0:
        return [1]
    my_tri = [1, 3]
    for i in range(2, n + 1):
        if i % 2 == 0:
            my_tri.append(i / 2 + 1)
        else:
            my_tri.append(my_tri[i - 1] + my_tri[i - 2] + (i + 3) / 2)
    return my_tri

import pytest

def test_tri_base_case_n_0():
    # Base case when n is 0
    result = tri(0)
    expected = [1]
    assert result == expected

def test_tri_case_n_1():
    # Case when n is 1
    result = tri(1)
    expected = [1, 3]
    assert result == expected

def test_tri_case_n_2_even_index_append():
    # Case when n is 2 (even index append)
    result = tri(2)
    expected = [1, 3, 2.0]
    assert result == expected

def test_tri_case_n_3_odd_index_append_with_sum():
    # Case when n is 3 (odd index append with sum)
    result = tri(3)
    expected = [1, 3, 2.0, 8.0]
    assert result == expected

def test_tri_case_n_4_even_index_append():
    # Case when n is 4 (even index append)
    result = tri(4)
    expected = [1, 3, 2.0, 8.0, 3.0]
    assert result == expected

def test_tri_case_n_5_odd_index_append_with_sum():
    # Case when n is 5 (odd index append with sum)
    result = tri(5)
    expected = [1, 3, 2.0, 8.0, 3.0, 15.0]
    assert result == expected

def test_tri_case_n_6_even_index_append():
    # Case when n is 6 (even index append)
    result = tri(6)
    expected = [1, 3, 2.0, 8.0, 3.0, 15.0, 4.0]
    assert result == expected