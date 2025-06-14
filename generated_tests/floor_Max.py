def floor_Max(A,B,N):
    x = min(B - 1,N)
    return (A*x) // B

import pytest

def test_floor_Max_with_A5_B7_N10_corrected():
    # Scenario: Calculate floor_Max with A=5, B=7, N=10 where N > B-1 (corrected)
    A = 5
    B = 7
    N = 10
    expected_output = 4
    assert floor_Max(A, B, N) == expected_output

def test_floor_Max_with_A3_B5_N2():
    # Scenario: Calculate floor_Max with A=3, B=5, N=2 where N < B-1
    A = 3
    B = 5
    N = 2
    expected_output = 1
    assert floor_Max(A, B, N) == expected_output

def test_floor_Max_with_A10_B3_N1():
    # Scenario: Calculate floor_Max with A=10, B=3, N=1 where N < B-1
    A = 10
    B = 3
    N = 1
    expected_output = 3
    assert floor_Max(A, B, N) == expected_output

def test_floor_Max_with_A0_B10_N5():
    # Scenario: Calculate floor_Max with A=0, B=10, N=5 where A is zero
    A = 0
    B = 10
    N = 5
    expected_output = 0
    assert floor_Max(A, B, N) == expected_output

def test_floor_Max_with_A7_B1_N10():
    # Scenario: Calculate floor_Max with A=7, B=1, N=10 where B=1
    A = 7
    B = 1
    N = 10
    expected_output = 0
    assert floor_Max(A, B, N) == expected_output

def test_floor_Max_with_A8_B4_N3():
    # Scenario: Calculate floor_Max with A=8, B=4, N=3 where N = B-1
    A = 8
    B = 4
    N = 3
    expected_output = 6
    assert floor_Max(A, B, N) == expected_output