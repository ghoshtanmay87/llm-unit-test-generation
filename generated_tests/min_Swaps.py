def min_Swaps(s1,s2) :  
    c0 = 0; c1 = 0;  
    for i in range(len(s1)) :  
        if (s1[i] == '0' and s2[i] == '1') : 
            c0 += 1;    
        elif (s1[i] == '1' and s2[i] == '0') : 
            c1 += 1;  
    result = c0 // 2 + c1 // 2;  
    if (c0 % 2 == 0 and c1 % 2 == 0) : 
        return result;  
    elif ((c0 + c1) % 2 == 0) : 
        return result + 2;  
    else : 
        return -1;

import pytest

def test_identical_strings_no_swaps_needed():
    s1 = '1100'
    s2 = '1100'
    expected = 0
    assert min_Swaps(s1, s2) == expected

def test_one_pair_mismatched_bits_swapped_directly_case1():
    s1 = '01'
    s2 = '10'
    expected = 2
    assert min_Swaps(s1, s2) == expected

def test_mismatches_only_one_direction_even_count():
    s1 = '0000'
    s2 = '1111'
    expected = 2
    assert min_Swaps(s1, s2) == expected

def test_mismatches_only_one_direction_odd_count():
    s1 = '000'
    s2 = '111'
    expected = -1
    assert min_Swaps(s1, s2) == expected

def test_mixed_mismatches_even_counts():
    s1 = '0101'
    s2 = '1010'
    expected = 2
    assert min_Swaps(s1, s2) == expected

def test_mixed_mismatches_odd_counts_sum_odd():
    s1 = '010'
    s2 = '101'
    expected = -1
    assert min_Swaps(s1, s2) == expected

def test_mixed_mismatches_odd_counts_sum_even():
    s1 = '010'
    s2 = '100'
    expected = 2
    assert min_Swaps(s1, s2) == expected