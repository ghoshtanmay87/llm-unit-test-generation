def fibonacci(n):
  if n == 1 or n == 2:
    return 1
  else:
    return (fibonacci(n - 1) + (fibonacci(n - 2)))

import pytest

def test_fibonacci_1st_number():
    # Calculate the 1st Fibonacci number
    # For n=1, the function returns 1 directly as per the base case.
    assert fibonacci(1) == 1

def test_fibonacci_2nd_number():
    # Calculate the 2nd Fibonacci number
    # For n=2, the function returns 1 directly as per the base case.
    assert fibonacci(2) == 1

def test_fibonacci_3rd_number():
    # Calculate the 3rd Fibonacci number
    # For n=3, the function returns fibonacci(2) + fibonacci(1) = 1 + 1 = 2.
    assert fibonacci(3) == 2

def test_fibonacci_4th_number():
    # Calculate the 4th Fibonacci number
    # For n=4, the function returns fibonacci(3) + fibonacci(2) = 2 + 1 = 3.
    assert fibonacci(4) == 3

def test_fibonacci_5th_number():
    # Calculate the 5th Fibonacci number
    # For n=5, the function returns fibonacci(4) + fibonacci(3) = 3 + 2 = 5.
    assert fibonacci(5) == 5

def test_fibonacci_6th_number():
    # Calculate the 6th Fibonacci number
    # For n=6, the function returns fibonacci(5) + fibonacci(4) = 5 + 3 = 8.
    assert fibonacci(6) == 8