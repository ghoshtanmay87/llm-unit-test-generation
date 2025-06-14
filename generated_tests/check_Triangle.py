def check_Triangle(x1,y1,x2,y2,x3,y3): 
    a = (x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))   
    if a == 0: 
        return ('No') 
    else: 
        return ('Yes')

import pytest

def test_collinear_points_on_x_axis():
    # All three points are collinear on the x-axis
    result = check_Triangle(0, 0, 1, 0, 2, 0)
    assert result == "No"

def test_valid_triangle_positive_area():
    # Points form a valid triangle with positive area
    result = check_Triangle(0, 0, 1, 0, 0, 1)
    assert result == "Yes"

def test_collinear_points_on_diagonal():
    # Points are collinear on a diagonal line
    result = check_Triangle(1, 1, 2, 2, 3, 3)
    assert result == "No"

def test_triangle_with_negative_area_orientation():
    # Points form a triangle with negative area (orientation)
    result = check_Triangle(0, 0, 0, 1, 1, 0)
    assert result == "Yes"

def test_two_points_same_no_triangle():
    # Two points are the same, so no triangle
    result = check_Triangle(0, 0, 0, 0, 1, 1)
    assert result == "No"