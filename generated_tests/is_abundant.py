def is_abundant(n):
    fctrsum = sum([fctr for fctr in range(1, n) if n % fctr == 0])
    return fctrsum > n

import pytest

def test_is_abundant_with_12():
    # The proper divisors of 12 are 1, 2, 3, 4, and 6. Their sum is 16, which is greater than 12, so 12 is abundant.
    assert is_abundant(12) is True

def test_is_abundant_with_15():
    # The proper divisors of 15 are 1, 3, and 5. Their sum is 9, which is less than 15, so 15 is not abundant.
    assert is_abundant(15) is False

def test_is_abundant_with_6():
    # The proper divisors of 6 are 1, 2, and 3. Their sum is 6, which is equal to 6, so 6 is not abundant.
    assert is_abundant(6) is False

def test_is_abundant_with_18():
    # The proper divisors of 18 are 1, 2, 3, 6, and 9. Their sum is 21, which is greater than 18, so 18 is abundant.
    assert is_abundant(18) is True

def test_is_abundant_with_1():
    # The number 1 has no proper divisors other than itself, so the sum is 0, which is less than 1, so 1 is not abundant.
    assert is_abundant(1) is False