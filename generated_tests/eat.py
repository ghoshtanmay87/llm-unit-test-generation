def eat(number, need, remaining):
    if need <= remaining:
        return [number + need, remaining - need]
    else:
        return [number + remaining, 0]

import pytest

def test_eat_need_less_than_remaining():
    # Need is less than remaining
    result = eat(number=10, need=5, remaining=20)
    assert result == [15, 15]

def test_eat_need_equal_to_remaining():
    # Need is equal to remaining
    result = eat(number=7, need=3, remaining=3)
    assert result == [10, 0]

def test_eat_need_greater_than_remaining():
    # Need is greater than remaining
    result = eat(number=4, need=10, remaining=6)
    assert result == [10, 0]

def test_eat_need_is_zero():
    # Need is zero
    result = eat(number=8, need=0, remaining=5)
    assert result == [8, 5]

def test_eat_remaining_is_zero():
    # Remaining is zero
    result = eat(number=3, need=4, remaining=0)
    assert result == [3, 0]