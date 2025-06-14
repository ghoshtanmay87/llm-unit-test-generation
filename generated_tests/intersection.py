def intersection(interval1, interval2):

    def is_prime(num):
        if num == 1 or num == 0:
            return False
        if num == 2:
            return True
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    l = max(interval1[0], interval2[0])
    r = min(interval1[1], interval2[1])
    length = r - l
    if length > 0 and is_prime(length):
        return 'YES'
    return 'NO'

import pytest

def test_intersection_length_prime_number():
    # Intervals with intersection length that is a prime number
    interval1 = [1, 5]
    interval2 = [3, 7]
    expected = 'YES'
    assert intersection(interval1, interval2) == expected

def test_intersection_no_intersection():
    # Intervals with no intersection
    interval1 = [1, 2]
    interval2 = [3, 4]
    expected = 'NO'
    assert intersection(interval1, interval2) == expected

def test_intersection_length_zero():
    # Intervals with intersection length zero
    interval1 = [1, 3]
    interval2 = [3, 5]
    expected = 'NO'
    assert intersection(interval1, interval2) == expected

def test_intersection_length_not_prime_4():
    # Intervals with intersection length that is not prime (4)
    interval1 = [1, 7]
    interval2 = [3, 7]
    expected = 'NO'
    assert intersection(interval1, interval2) == expected

def test_intersection_length_1_not_prime():
    # Intervals with intersection length 1 (not prime)
    interval1 = [2, 3]
    interval2 = [2, 4]
    expected = 'NO'
    assert intersection(interval1, interval2) == expected

def test_intersection_length_5_prime():
    # Intervals with intersection length 5 (prime)
    interval1 = [0, 10]
    interval2 = [5, 10]
    expected = 'YES'
    assert intersection(interval1, interval2) == expected

def test_intersection_length_3_prime():
    # Intervals with intersection length that is not a prime number (actually prime 3)
    interval1 = [1, 6]
    interval2 = [3, 7]
    expected = 'YES'
    assert intersection(interval1, interval2) == expected