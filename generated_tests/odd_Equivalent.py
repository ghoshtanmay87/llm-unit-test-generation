def odd_Equivalent(s,n): 
    count=0
    for i in range(0,n): 
        if (s[i] == '1'): 
            count = count + 1
    return count

import pytest

def test_count_ones_in_mixed_characters():
    # Count number of '1's in a string of length 5 with mixed characters
    s = '10101'
    n = 5
    expected = 3
    assert odd_Equivalent(s, n) == expected

def test_count_ones_in_string_with_no_ones():
    # Count number of '1's in a string of length 4 with no '1's
    s = '0000'
    n = 4
    expected = 0
    assert odd_Equivalent(s, n) == expected

def test_count_ones_in_all_ones_string():
    # Count number of '1's in a string of length 3 with all '1's
    s = '111'
    n = 3
    expected = 3
    assert odd_Equivalent(s, n) == expected

def test_count_ones_in_alternating_characters():
    # Count number of '1's in a string of length 6 with alternating characters
    s = '010101'
    n = 6
    expected = 3
    assert odd_Equivalent(s, n) == expected

def test_count_ones_in_empty_substring():
    # Count number of '1's in a string of length 0 (empty substring)
    s = '10101'
    n = 0
    expected = 0
    assert odd_Equivalent(s, n) == expected