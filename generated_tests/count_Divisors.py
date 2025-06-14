import math 
def count_Divisors(n) : 
    count = 0
    for i in range(1, (int)(math.sqrt(n)) + 2) : 
        if (n % i == 0) : 
            if( n // i == i) : 
                count = count + 1
            else : 
                count = count + 2
    if (count % 2 == 0) : 
        return ("Even") 
    else : 
        return ("Odd")

import pytest

def test_divisors_count_parity_n_1():
    # 1 has exactly one divisor (1). Count=1, which is odd.
    assert count_Divisors(1) == "Odd"

def test_divisors_count_parity_n_4_perfect_square():
    # 4 has divisors 1,2,4. Count=3, which is odd.
    assert count_Divisors(4) == "Odd"

def test_divisors_count_parity_n_6_non_perfect_square():
    # 6 has divisors 1,2,3,6. Count=4, which is even.
    assert count_Divisors(6) == "Even"

def test_divisors_count_parity_n_10_non_perfect_square():
    # 10 has divisors 1,2,5,10. Count=4, which is even.
    assert count_Divisors(10) == "Even"

def test_divisors_count_parity_n_16_perfect_square():
    # 16 has divisors 1,2,4,8,16. Count=5, which is odd.
    assert count_Divisors(16) == "Odd"

def test_divisors_count_parity_n_25_perfect_square():
    # 25 has divisors 1,5,25. Count=3, which is odd.
    assert count_Divisors(25) == "Odd"

def test_divisors_count_parity_n_12_non_perfect_square():
    # 12 has divisors 1,2,3,4,6,12. Count=6, which is even.
    assert count_Divisors(12) == "Even"