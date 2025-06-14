def count_Rectangles(radius):  
    rectangles = 0 
    diameter = 2 * radius 
    diameterSquare = diameter * diameter 
    for a in range(1, 2 * radius):  
        for b in range(1, 2 * radius): 
            diagnalLengthSquare = (a * a +  b * b)  
            if (diagnalLengthSquare <= diameterSquare) : 
                rectangles += 1
    return rectangles

import pytest

def test_count_rectangles_radius_1():
    # Scenario: Count rectangles for radius 1
    radius = 1
    expected_output = 1
    assert count_Rectangles(radius) == expected_output

def test_count_rectangles_radius_2():
    # Scenario: Count rectangles for radius 2
    radius = 2
    expected_output = 13
    assert count_Rectangles(radius) == expected_output

def test_count_rectangles_radius_3():
    # Scenario: Count rectangles for radius 3
    radius = 3
    expected_output = 29
    assert count_Rectangles(radius) == expected_output

def test_count_rectangles_radius_0_edge_case():
    # Scenario: Count rectangles for radius 0 (edge case)
    radius = 0
    expected_output = 0
    assert count_Rectangles(radius) == expected_output

def test_count_rectangles_radius_4():
    # Scenario: Count rectangles for radius 4
    radius = 4
    expected_output = 49
    assert count_Rectangles(radius) == expected_output