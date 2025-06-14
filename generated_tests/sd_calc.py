import math
import sys
def sd_calc(data):
    n = len(data)
    if n <= 1:
        return 0.0
    mean, sd = avg_calc(data), 0.0
    for el in data:
        sd += (float(el) - mean)**2
    sd = math.sqrt(sd / float(n-1))
    return sd
def avg_calc(ls):
    n, mean = len(ls), 0.0
    if n <= 1:
        return ls[0]
    for el in ls:
        mean = mean + float(el)
    mean = mean / float(n)
    return mean

import pytest

def test_sd_calc_multiple_elements():
    data = [2, 4, 4, 4, 5, 5, 7, 9]
    expected_output = 2.138089935299395
    assert sd_calc(data) == expected_output

def test_sd_calc_single_element():
    data = [10]
    expected_output = 0.0
    assert sd_calc(data) == expected_output

def test_sd_calc_two_elements():
    data = [10, 14]
    expected_output = 2.8284271247461903
    assert sd_calc(data) == expected_output

def test_sd_calc_identical_elements():
    data = [5, 5, 5, 5]
    expected_output = 0.0
    assert sd_calc(data) == expected_output

def test_sd_calc_negative_and_positive_numbers():
    data = [-3, -1, 0, 1, 3]
    expected_output = 2.23606797749979
    assert sd_calc(data) == expected_output