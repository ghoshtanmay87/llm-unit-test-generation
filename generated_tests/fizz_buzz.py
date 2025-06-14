def fizz_buzz(n: int):
    ns = []
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            ns.append(i)
    s = ''.join(list(map(str, ns)))
    ans = 0
    for c in s:
        ans += c == '7'
    return ans

import pytest

def test_input_zero_returns_zero():
    # Input zero returns zero since no numbers are processed
    n = 0
    expected = 0
    assert fizz_buzz(n) == expected

def test_input_one_returns_zero():
    # Input one returns zero because 0 is divisible by 11 and 13 and contains zero '7's
    n = 1
    expected = 0
    assert fizz_buzz(n) == expected

def test_input_fourteen_counts_zero_sevens():
    # Input fourteen counts '7's in numbers divisible by 11 or 13 below 14, expected zero '7's
    n = 14
    expected = 0
    assert fizz_buzz(n) == expected

def test_input_twenty_counts_zero_sevens():
    # Input twenty counts '7's in numbers divisible by 11 or 13 below 20, expected zero '7's
    n = 20
    expected = 0
    assert fizz_buzz(n) == expected

def test_input_seventy_counts_zero_sevens():
    # Input seventy counts '7's in numbers divisible by 11 or 13 below 70, expected zero '7's
    n = 70
    expected = 0
    assert fizz_buzz(n) == expected

def test_input_hundred_counts_three_sevens():
    # Input 100 counts '7's in numbers divisible by 11 or 13 below 100, expected three '7's
    n = 100
    expected = 3
    assert fizz_buzz(n) == expected