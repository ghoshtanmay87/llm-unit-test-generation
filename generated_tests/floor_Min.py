def floor_Min(A,B,N):
    x = max(B - 1,N)
    return (A*x) // B

import pytest

def test_when_B_is_less_than_N_x_is_set_to_N():
    # Scenario: When B is less than N, x is set to N
    A = 10
    B = 3
    N = 5
    expected_output = 50
    assert floor_Min(A, B, N) == expected_output

def test_when_B_minus_1_is_greater_than_N_x_is_set_to_B_minus_1():
    # Scenario: When B-1 is greater than N, x is set to B-1
    A = 7
    B = 10
    N = 5
    expected_output = 63
    assert floor_Min(A, B, N) == expected_output

def test_when_B_minus_1_equals_N_x_is_set_to_B_minus_1_or_N():
    # Scenario: When B-1 equals N, x is set to B-1 (or N)
    A = 4
    B = 6
    N = 5
    expected_output = 3
    assert floor_Min(A, B, N) == expected_output

def test_when_B_is_1_x_is_max_0_N_which_is_N():
    # Scenario: When B is 1, x is max(0, N) which is N
    A = 8
    B = 1
    N = 4
    expected_output = 32
    assert floor_Min(A, B, N) == expected_output

def test_when_A_B_and_N_are_all_equal():
    # Scenario: When A, B, and N are all equal
    A = 5
    B = 5
    N = 5
    expected_output = 20
    assert floor_Min(A, B, N) == expected_output

def test_when_N_is_zero_and_B_greater_than_1():
    # Scenario: When N is zero and B > 1
    A = 9
    B = 4
    N = 0
    expected_output = 18
    assert floor_Min(A, B, N) == expected_output