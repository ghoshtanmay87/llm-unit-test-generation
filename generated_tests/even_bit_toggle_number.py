def even_bit_toggle_number(n) : 
    res = 0; count = 0; temp = n    
    while(temp > 0 ) : 
        if (count % 2 == 0) : 
            res = res | (1 << count)      
        count = count + 1
        temp >>= 1 
    return n ^ res

import pytest

def test_toggle_bits_even_positions_n_zero():
    # Scenario: Toggle bits at even positions for n=0
    n = 0
    expected_output = 0
    assert even_bit_toggle_number(n) == expected_output

def test_toggle_bits_even_positions_n_one():
    # Scenario: Toggle bits at even positions for n=1 (binary 1)
    n = 1
    expected_output = 0
    assert even_bit_toggle_number(n) == expected_output

def test_toggle_bits_even_positions_n_two():
    # Scenario: Toggle bits at even positions for n=2 (binary 10)
    n = 2
    expected_output = 3
    assert even_bit_toggle_number(n) == expected_output

def test_toggle_bits_even_positions_n_five():
    # Scenario: Toggle bits at even positions for n=5 (binary 101)
    n = 5
    expected_output = 0
    assert even_bit_toggle_number(n) == expected_output

def test_toggle_bits_even_positions_n_ten():
    # Scenario: Toggle bits at even positions for n=10 (binary 1010)
    n = 10
    expected_output = 5
    assert even_bit_toggle_number(n) == expected_output

def test_toggle_bits_even_positions_n_fifteen():
    # Scenario: Toggle bits at even positions for n=15 (binary 1111)
    n = 15
    expected_output = 10
    assert even_bit_toggle_number(n) == expected_output

def test_toggle_bits_even_positions_n_twentyone():
    # Scenario: Toggle bits at even positions for n=21 (binary 10101)
    n = 21
    expected_output = 16
    assert even_bit_toggle_number(n) == expected_output

def test_toggle_bits_even_positions_n_thirtytwo():
    # Scenario: Toggle bits at even positions for n=32 (binary 100000)
    n = 32
    expected_output = 63
    assert even_bit_toggle_number(n) == expected_output