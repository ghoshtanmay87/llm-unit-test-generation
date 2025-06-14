def prime_num(num):
  if num >=1:
   for i in range(2, num//2):
     if (num % i) == 0:
                return False
     else:
                return True
  else:
          return False

import pytest

def test_prime_num_with_1():
    # Check if 1 is prime
    result = prime_num(num=1)
    assert result is False

def test_prime_num_with_2():
    # Check if 2 is prime
    result = prime_num(num=2)
    assert result is False

def test_prime_num_with_3():
    # Check if 3 is prime
    result = prime_num(num=3)
    assert result is False

def test_prime_num_with_4():
    # Check if 4 is prime
    result = prime_num(num=4)
    assert result is False

def test_prime_num_with_6():
    # Check if 6 is prime
    result = prime_num(num=6)
    assert result is False

def test_prime_num_with_9():
    # Check if 9 is prime
    result = prime_num(num=9)
    assert result is True

def test_prime_num_with_10():
    # Check if 10 is prime
    result = prime_num(num=10)
    assert result is False

def test_prime_num_with_11():
    # Check if 11 is prime
    result = prime_num(num=11)
    assert result is True