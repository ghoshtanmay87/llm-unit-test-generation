def sum_Of_Series(n): 
    sum = 0
    for i in range(1,n + 1): 
        sum += i * i*i       
    return sum

import pytest

def test_sum_of_series_n_1():
    # Scenario: Sum of series for n=1
    # Reasoning: For n=1, the loop runs once with i=1. sum = 1*1*1 = 1.
    result = sum_Of_Series(1)
    assert result == 1

def test_sum_of_series_n_2():
    # Scenario: Sum of series for n=2
    # Reasoning: For n=2, sum = 1^3 + 2^3 = 1 + 8 = 9.
    result = sum_Of_Series(2)
    assert result == 9

def test_sum_of_series_n_3():
    # Scenario: Sum of series for n=3
    # Reasoning: For n=3, sum = 1^3 + 2^3 + 3^3 = 1 + 8 + 27 = 36.
    result = sum_Of_Series(3)
    assert result == 36

def test_sum_of_series_n_4():
    # Scenario: Sum of series for n=4
    # Reasoning: For n=4, sum = 1^3 + 2^3 + 3^3 + 4^3 = 1 + 8 + 27 + 64 = 100.
    result = sum_Of_Series(4)
    assert result == 100

def test_sum_of_series_n_5():
    # Scenario: Sum of series for n=5
    # Reasoning: For n=5, sum = 1^3 + 2^3 + 3^3 + 4^3 + 5^3 = 1 + 8 + 27 + 64 + 125 = 225.
    result = sum_Of_Series(5)
    assert result == 225