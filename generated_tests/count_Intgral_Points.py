def count_Intgral_Points(x1,y1,x2,y2): 
    return ((y2 - y1 - 1) * (x2 - x1 - 1))

import pytest

def test_count_integral_points_inside_rectangle_11_45():
    # Count integral points inside a rectangle defined by (11) and (45)
    result = count_Intgral_Points(1, 1, 4, 5)
    assert result == 6

def test_count_integral_points_inside_rectangle_00_33():
    # Count integral points inside a rectangle defined by (00) and (33)
    result = count_Intgral_Points(0, 0, 3, 3)
    assert result == 4

def test_count_integral_points_unit_square_no_interior():
    # Count integral points inside a rectangle where x2 - x1 = 1 and y2 - y1 = 1 (no interior points)
    result = count_Intgral_Points(2, 2, 3, 3)
    assert result == 0

def test_count_integral_points_with_negative_coordinates():
    # Count integral points inside a rectangle with negative coordinates
    result = count_Intgral_Points(-2, -2, 2, 2)
    assert result == 9

def test_count_integral_points_degenerate_x_axis():
    # Count integral points when rectangle is degenerate along x-axis (x1 == x2)
    result = count_Intgral_Points(5, 1, 5, 4)
    assert result == -2

def test_count_integral_points_degenerate_y_axis():
    # Count integral points when rectangle is degenerate along y-axis (y1 == y2)
    result = count_Intgral_Points(1, 3, 4, 3)
    assert result == -1