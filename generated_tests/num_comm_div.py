def ngcd(x,y):
    i=1
    while(i<=x and i<=y):
        if(x%i==0 and y%i == 0):
            gcd=i;
        i+=1
    return gcd;
def num_comm_div(x,y):
  n = ngcd(x,y)
  result = 0
  z = int(n**0.5)
  i = 1
  while(i <= z):
    if(n % i == 0):
      result += 2 
      if(i == n/i):
        result-=1
    i+=1
  return result

import pytest

def test_common_divisors_count_gcd_6():
    # The gcd of 12 and 18 is 6. The divisors of 6 are 1, 2, 3, and 6, so there are 4 common divisors.
    assert num_comm_div(12, 18) == 4

def test_common_divisors_count_gcd_1_coprime():
    # The gcd of 7 and 13 is 1. The only divisor of 1 is 1 itself, so there is exactly 1 common divisor.
    assert num_comm_div(7, 13) == 1

def test_common_divisors_count_two_equal_numbers():
    # The gcd of 10 and 10 is 10. The divisors of 10 are 1, 2, 5, and 10, so there are 4 common divisors.
    assert num_comm_div(10, 10) == 4

def test_common_divisors_count_gcd_1_prime_and_composite():
    # The gcd of 17 and 20 is 1. The only divisor of 1 is 1 itself, so there is exactly 1 common divisor.
    assert num_comm_div(17, 20) == 1

def test_common_divisors_count_gcd_12():
    # The gcd of 36 and 60 is 12. The divisors of 12 are 1, 2, 3, 4, 6, and 12, so there are 6 common divisors.
    assert num_comm_div(36, 60) == 6

def test_common_divisors_count_gcd_1_one_is_1():
    # The gcd of 1 and 100 is 1. The only divisor of 1 is 1 itself, so there is exactly 1 common divisor.
    assert num_comm_div(1, 100) == 1

def test_common_divisors_count_gcd_49_perfect_square():
    # The gcd of 49 and 98 is 49. The divisors of 49 are 1, 7, and 49. Since 49 is a perfect square, the function correctly counts 3 divisors.
    assert num_comm_div(49, 98) == 3