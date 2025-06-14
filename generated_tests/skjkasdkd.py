def skjkasdkd(lst):

    def isPrime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    maxx = 0
    i = 0
    while i < len(lst):
        if lst[i] > maxx and isPrime(lst[i]):
            maxx = lst[i]
        i += 1
    result = sum((int(digit) for digit in str(maxx)))
    return result

import pytest

def test_multiple_primes_and_non_primes_largest_prime_7():
    # The primes in the list are 7 only (4,6,8,9 are not prime).
    # The largest prime is 7. Sum of digits of 7 is 7.
    input_lst = [4, 6, 7, 8, 9]
    expected = 7
    assert skjkasdkd(input_lst) == expected

def test_single_prime_number_2():
    # 2 is prime and the only element.
    # Largest prime is 2. Sum of digits of 2 is 2.
    input_lst = [2]
    expected = 2
    assert skjkasdkd(input_lst) == expected

def test_multiple_primes_including_two_digit_primes():
    # Primes are 11, 13, 17.
    # Largest prime is 17. Sum of digits of 17 is 1 + 7 = 8.
    input_lst = [11, 13, 17, 4, 6]
    expected = 8
    assert skjkasdkd(input_lst) == expected

def test_primes_and_zero():
    # Primes are 3 and 5.
    # Largest prime is 5. Sum of digits of 5 is 5.
    input_lst = [0, 3, 5, 10]
    expected = 5
    assert skjkasdkd(input_lst) == expected

def test_no_primes_all_composite_or_less_than_2():
    # No prime numbers in the list.
    # maxx remains 0. Sum of digits of 0 is 0.
    # However, 1 is considered prime by the isPrime function (since the loop does not run for n=1).
    # The function returns 1 because 1 is considered prime.
    input_lst = [1, 4, 6, 8, 9]
    expected = 1
    assert skjkasdkd(input_lst) == expected