def check_Equality(s): 
    return (ord(s[0]) == ord(s[len(s) - 1])); 
def count_Substring_With_Equal_Ends(s): 
    result = 0; 
    n = len(s); 
    for i in range(n):
        for j in range(1,n-i+1): 
            if (check_Equality(s[i:i+j])): 
                result+=1; 
    return result;

import pytest

def test_count_substrings_equal_ends_simple_abc():
    # Scenario: Count substrings with equal start and end characters in a simple string 'abc'
    s = 'abc'
    expected = 3
    assert count_Substring_With_Equal_Ends(s) == expected

def test_count_substrings_equal_ends_all_aaa():
    # Scenario: Count substrings with equal start and end characters in string 'aaa'
    s = 'aaa'
    expected = 6
    assert count_Substring_With_Equal_Ends(s) == expected

def test_count_substrings_equal_ends_abca():
    # Scenario: Count substrings with equal start and end characters in string 'abca'
    s = 'abca'
    expected = 6
    assert count_Substring_With_Equal_Ends(s) == expected

def test_count_substrings_equal_ends_empty_string():
    # Scenario: Count substrings with equal start and end characters in empty string
    s = ''
    expected = 0
    assert count_Substring_With_Equal_Ends(s) == expected

def test_count_substrings_equal_ends_all_distinct_abcd():
    # Scenario: Count substrings with equal start and end characters in string with all distinct characters 'abcd'
    s = 'abcd'
    expected = 4
    assert count_Substring_With_Equal_Ends(s) == expected