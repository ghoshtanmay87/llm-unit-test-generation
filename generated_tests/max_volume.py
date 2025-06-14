def max_volume (s): 
    maxvalue = 0
    i = 1
    for i in range(s - 1): 
        j = 1
        for j in range(s): 
            k = s - i - j 
            maxvalue = max(maxvalue, i * j * k)         
    return maxvalue

import pytest

def test_max_volume_minimum_input_s_1():
    # Calculate max volume for s=1 (minimum input)
    result = max_volume(1)
    assert result == 0

def test_max_volume_s_2():
    # Calculate max volume for s=2
    result = max_volume(2)
    assert result == 0

def test_max_volume_s_3():
    # Calculate max volume for s=3
    result = max_volume(3)
    assert result == 1

def test_max_volume_s_4():
    # Calculate max volume for s=4
    result = max_volume(4)
    assert result == 4

def test_max_volume_s_5():
    # Calculate max volume for s=5
    result = max_volume(5)
    assert result == 6

def test_max_volume_s_10():
    # Calculate max volume for s=10
    result = max_volume(10)
    assert result == 96