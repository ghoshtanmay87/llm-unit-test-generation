def harmonic_sum(n):
  if n < 2:
    return 1
  else:
    return 1 / n + (harmonic_sum(n - 1))

import pytest

def test_harmonic_sum_n_1():
    # Calculate harmonic sum for n=1
    result = harmonic_sum(1)
    assert result == 1, "Expected harmonic_sum(1) to be 1"

def test_harmonic_sum_n_2():
    # Calculate harmonic sum for n=2
    result = harmonic_sum(2)
    assert result == 1.5, "Expected harmonic_sum(2) to be 1.5"

def test_harmonic_sum_n_3():
    # Calculate harmonic sum for n=3
    result = harmonic_sum(3)
    assert result == 1.8333333333333333, "Expected harmonic_sum(3) to be 1.8333333333333333"

def test_harmonic_sum_n_4():
    # Calculate harmonic sum for n=4
    result = harmonic_sum(4)
    assert result == 2.083333333333333, "Expected harmonic_sum(4) to be 2.083333333333333"

def test_harmonic_sum_n_5():
    # Calculate harmonic sum for n=5
    result = harmonic_sum(5)
    assert result == 2.283333333333333, "Expected harmonic_sum(5) to be 2.283333333333333"