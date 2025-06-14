import math 
def divSum(n): 
    sum = 1; 
    i = 2; 
    while(i * i <= n): 
        if (n % i == 0): 
            sum = (sum + i +math.floor(n / i)); 
        i += 1; 
    return sum; 
def areEquivalent(num1,num2): 
    return divSum(num1) == divSum(num2);

import pytest

def test_equivalence_two_equal_prime_numbers():
    # 7 is prime, divSum(7) = 1, both inputs same, sums equal
    assert areEquivalent(7, 7) is True

def test_equivalence_two_different_prime_numbers():
    # Both 7 and 11 are prime, divSum(7) = 1, divSum(11) = 1, sums equal
    assert areEquivalent(7, 11) is True

def test_equivalence_two_numbers_same_divisor_sum():
    # divSum(6) = 6, divSum(25) = 6, sums equal
    assert areEquivalent(6, 25) is True

def test_equivalence_two_numbers_different_divisor_sums():
    # divSum(8) = 7, divSum(9) = 4, sums differ
    assert areEquivalent(8, 9) is False

def test_equivalence_number_and_itself():
    # divSum(12) = 16, same number, sums equal
    assert areEquivalent(12, 12) is True

def test_equivalence_perfect_and_non_perfect_number():
    # divSum(28) = 28, divSum(12) = 16, sums differ
    assert areEquivalent(28, 12) is False