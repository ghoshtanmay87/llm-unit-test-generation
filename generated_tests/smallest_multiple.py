def smallest_multiple(n):
    if (n<=2):
      return n
    i = n * 2
    factors = [number  for number in range(n, 1, -1) if number * 2 > n]
    while True:
        for a in factors:
            if i % a != 0:
                i += n
                break
            if (a == factors[-1] and i % a == 0):
                return i

import pytest

def test_smallest_multiple_n_1():
    # Since n is less than or equal to 2, the function returns n directly, so output is 1.
    assert smallest_multiple(1) == 1

def test_smallest_multiple_n_2():
    # Since n is less than or equal to 2, the function returns n directly, so output is 2.
    assert smallest_multiple(2) == 2

def test_smallest_multiple_n_3():
    # Factors are [3, 2]. Starting from i=6, 6 is divisible by both 3 and 2, so output is 6.
    assert smallest_multiple(3) == 6

def test_smallest_multiple_n_4():
    # Factors are [4, 3, 2]. Starting from i=8, 8 is not divisible by 3, increment by 4 to 12,
    # which is divisible by 4, 3, and 2, so output is 12.
    assert smallest_multiple(4) == 12

def test_smallest_multiple_n_5():
    # Factors are [5, 4, 3]. After checking multiples starting from 10, 60 is divisible by 5, 4, and 3.
    assert smallest_multiple(5) == 60

def test_smallest_multiple_n_6():
    # Factors are [6, 5, 4]. After checking multiples starting from 12, 60 is divisible by 6, 5, and 4.
    assert smallest_multiple(6) == 60