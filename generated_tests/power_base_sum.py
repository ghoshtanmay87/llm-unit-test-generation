def power_base_sum(base, power):
    return sum([int(i) for i in str(pow(base, power))])

import pytest

def test_sum_of_digits_2_power_3():
    # 2^3 = 8, digits are [8], sum is 8
    assert power_base_sum(2, 3) == 8

def test_sum_of_digits_10_power_2():
    # 10^2 = 100, digits are [1,0,0], sum is 1+0+0=1
    assert power_base_sum(10, 2) == 1

def test_sum_of_digits_5_power_4():
    # 5^4 = 625, digits are [6,2,5], sum is 6+2+5=13
    # Note: expected_output in user story is 7, but reasoning says sum is 13.
    # Following instructions to trust expected_output as correct.
    assert power_base_sum(5, 4) == 7

def test_sum_of_digits_3_power_5():
    # 3^5 = 243, digits are [2,4,3], sum is 2+4+3=9
    assert power_base_sum(3, 5) == 9

def test_sum_of_digits_0_power_0():
    # 0^0 is defined as 1 in Python, digits are [1], sum is 1
    assert power_base_sum(0, 0) == 1

def test_sum_of_digits_1_power_1000():
    # 1^1000 = 1, digits are [1], sum is 1
    assert power_base_sum(1, 1000) == 1

def test_sum_of_digits_9_power_2():
    # 9^2 = 81, digits are [8,1], sum is 8+1=9
    assert power_base_sum(9, 2) == 9