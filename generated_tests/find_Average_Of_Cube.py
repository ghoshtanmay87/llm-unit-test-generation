def find_Average_Of_Cube(n):  
    sum = 0
    for i in range(1, n + 1): 
        sum += i * i * i  
    return round(sum / n, 6)

import pytest

def test_average_of_cubes_n_1():
    # Calculate average of cubes for n=1
    result = find_Average_Of_Cube(1)
    assert result == 1.0

def test_average_of_cubes_n_2():
    # Calculate average of cubes for n=2
    result = find_Average_Of_Cube(2)
    assert result == 4.5

def test_average_of_cubes_n_3_corrected():
    # Calculate average of cubes for n=3 (corrected)
    result = find_Average_Of_Cube(3)
    assert result == 12.0

def test_average_of_cubes_n_4_corrected():
    # Calculate average of cubes for n=4 (corrected)
    result = find_Average_Of_Cube(4)
    assert result == 25.0

def test_average_of_cubes_n_5_corrected():
    # Calculate average of cubes for n=5 (corrected)
    result = find_Average_Of_Cube(5)
    assert result == 45.0

def test_average_of_cubes_n_10():
    # Calculate average of cubes for n=10
    result = find_Average_Of_Cube(10)
    assert result == 302.5