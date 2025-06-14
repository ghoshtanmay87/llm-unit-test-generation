def hex_key(num):
    primes = ('2', '3', '5', '7', 'B', 'D')
    total = 0
    for i in range(0, len(num)):
        if num[i] in primes:
            total += 1
    return total

import pytest

def test_count_prime_hex_digits_mixed_characters():
    # All characters '2', '3', '5', '7', 'B', 'D' are in the primes tuple, so total count is 6.
    assert hex_key('2357BD') == 6

def test_count_prime_hex_digits_no_prime_characters():
    # None of the characters '1', '4', '6', '8', '9', 'A', 'C', 'F' are in the primes tuple, so total count is 0.
    assert hex_key('14689ACF') == 0

def test_count_prime_hex_digits_empty_string():
    # Empty string has no characters, so total count is 0.
    assert hex_key('') == 0

def test_count_prime_hex_digits_repeated_prime_characters():
    # All characters are in primes: '2', '3', '5', '7', 'B'; total count is length of string 15.
    assert hex_key('222333555777BBB') == 15

def test_count_prime_hex_digits_some_prime_some_nonprime():
    # Characters '2', '3', '5', '7', 'B', and 'D' are in primes; all appear in the string, total count is 6.
    assert hex_key('123456789ABCDEF') == 6

def test_count_prime_hex_digits_lowercase_letters():
    # The primes tuple contains uppercase letters only; lowercase 'b' and 'd' do not match,
    # so only '2', '3', '5', '7' count, total 4.
    assert hex_key('2357bd') == 4