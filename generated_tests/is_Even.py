def is_Even(n) : 
    if (n^1 == n+1) :
        return True; 
    else :
        return False;

import pytest

def test_is_even_with_2():
    # Check if 2 is even
    # For n=2, n^1 = 3 and n+1 = 3, so n^1 == n+1 is True, thus the function returns True.
    assert is_Even(2) is True

def test_is_even_with_3():
    # Check if 3 is even
    # For n=3, n^1 = 2 and n+1 = 4, so n^1 == n+1 is False, thus the function returns False.
    assert is_Even(3) is False

def test_is_even_with_0():
    # Check if 0 is even
    # For n=0, n^1 = 1 and n+1 = 1, so n^1 == n+1 is True, thus the function returns True.
    assert is_Even(0) is True

def test_is_even_with_1():
    # Check if 1 is even
    # For n=1, n^1 = 0 and n+1 = 2, so n^1 == n+1 is False, thus the function returns False.
    assert is_Even(1) is False

def test_is_even_with_10():
    # Check if 10 is even
    # For n=10, n^1 = 11 and n+1 = 11, so n^1 == n+1 is True, thus the function returns True.
    assert is_Even(10) is True

def test_is_even_with_11():
    # Check if 11 is even
    # For n=11, n^1 = 10 and n+1 = 12, so n^1 == n+1 is False, thus the function returns False.
    assert is_Even(11) is False