def f(n):
    ret = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            x = 1
            for j in range(1, i + 1):
                x *= j
            ret += [x]
        else:
            x = 0
            for j in range(1, i + 1):
                x += j
            ret += [x]
    return ret

import pytest

def test_f_with_n_1_smallest_input():
    # Test with n=1, smallest input
    result = f(1)
    expected = [1]
    assert result == expected

def test_f_with_n_2_one_odd_one_even():
    # Test with n=2, includes one odd and one even
    result = f(2)
    expected = [1, 2]
    assert result == expected

def test_f_with_n_3_mix_odd_even():
    # Test with n=3, mix of odd and even numbers
    result = f(3)
    expected = [1, 2, 6]
    assert result == expected

def test_f_with_n_4_two_even_numbers():
    # Test with n=4, includes two even numbers
    result = f(4)
    expected = [1, 2, 6, 24]
    assert result == expected

def test_f_with_n_5_larger_mixed_input():
    # Test with n=5, larger input with mixed odd and even
    result = f(5)
    expected = [1, 2, 6, 24, 15]
    assert result == expected

def test_f_with_n_6_multiple_factorials_and_sums():
    # Test with n=6, includes multiple factorials and sums
    result = f(6)
    expected = [1, 2, 6, 24, 15, 720]
    assert result == expected