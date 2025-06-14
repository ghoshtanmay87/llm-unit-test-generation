def fib4(n: int):
    results = [0, 0, 2, 0]
    if n < 4:
        return results[n]
    for _ in range(4, n + 1):
        results.append(results[-1] + results[-2] + results[-3] + results[-4])
        results.pop(0)
    return results[-1]

import pytest

def test_fib4_input_0_returns_0():
    # Input less than 4 returns predefined values
    assert fib4(0) == 0

def test_fib4_input_1_returns_0():
    # Input less than 4 returns predefined values
    assert fib4(1) == 0

def test_fib4_input_2_returns_2():
    # Input less than 4 returns predefined values
    assert fib4(2) == 2

def test_fib4_input_3_returns_0():
    # Input less than 4 returns predefined values
    assert fib4(3) == 0

def test_fib4_input_4_returns_2():
    # Calculate fib4 for n=4
    assert fib4(4) == 2

def test_fib4_input_5_returns_4():
    # Calculate fib4 for n=5
    assert fib4(5) == 4

def test_fib4_input_6_returns_8():
    # Calculate fib4 for n=6
    assert fib4(6) == 8

def test_fib4_input_7_returns_14():
    # Calculate fib4 for n=7
    assert fib4(7) == 14

def test_fib4_input_8_returns_28():
    # Calculate fib4 for n=8
    assert fib4(8) == 28

def test_fib4_input_10_returns_104():
    # Calculate fib4 for n=10
    assert fib4(10) == 104