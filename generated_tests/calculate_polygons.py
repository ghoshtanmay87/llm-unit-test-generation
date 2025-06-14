import math
def calculate_polygons(startx, starty, endx, endy, radius):
    sl = (2 * radius) * math.tan(math.pi / 6)
    p = sl * 0.5
    b = sl * math.cos(math.radians(30))
    w = b * 2
    h = 2 * sl   
    startx = startx - w
    starty = starty - h
    endx = endx + w
    endy = endy + h
    origx = startx
    origy = starty
    xoffset = b
    yoffset = 3 * p
    polygons = []
    row = 1
    counter = 0
    while starty < endy:
        if row % 2 == 0:
            startx = origx + xoffset
        else:
            startx = origx
        while startx < endx:
            p1x = startx
            p1y = starty + p
            p2x = startx
            p2y = starty + (3 * p)
            p3x = startx + b
            p3y = starty + h
            p4x = startx + w
            p4y = starty + (3 * p)
            p5x = startx + w
            p5y = starty + p
            p6x = startx + b
            p6y = starty
            poly = [
                (p1x, p1y),
                (p2x, p2y),
                (p3x, p3y),
                (p4x, p4y),
                (p5x, p5y),
                (p6x, p6y),
                (p1x, p1y)]
            polygons.append(poly)
            counter += 1
            startx += w
        starty += yoffset
        row += 1
    return polygons

import pytest

def test_calculate_polygons_small_square_radius_1():
    result = calculate_polygons(startx=0, starty=0, endx=2, endy=2, radius=1)
    expected = [
        [(-1.7320508075688774, -0.5), (-1.7320508075688774, 1.5), (-0.8660254037844387, 3.0), (0.8660254037844387, 1.5), (0.8660254037844387, -0.5), (-0.8660254037844387, -2.0), (-1.7320508075688774, -0.5)],
        [(-0.8660254037844387, 0.5), (-0.8660254037844387, 2.5), (0.0, 4.0), (1.7320508075688774, 2.5), (1.7320508075688774, 0.5), (0.0, -1.0), (-0.8660254037844387, 0.5)]
    ]
    assert result == expected

def test_calculate_polygons_zero_area_radius_1():
    result = calculate_polygons(startx=0, starty=0, endx=0, endy=0, radius=1)
    expected = [
        [(-1.7320508075688774, -0.5), (-1.7320508075688774, 1.5), (-0.8660254037844387, 3.0), (0.8660254037844387, 1.5), (0.8660254037844387, -0.5), (-0.8660254037844387, -2.0), (-1.7320508075688774, -0.5)]
    ]
    assert result == expected

def test_calculate_polygons_larger_rectangle_radius_2():
    result = calculate_polygons(startx=0, starty=0, endx=5, endy=3, radius=2)
    expected = [
        [(-3.464101615137755, -1.0), (-3.464101615137755, 4.0), (-1.7320508075688772, 6.0), (1.7320508075688772, 4.0), (1.7320508075688772, -1.0), (-1.7320508075688772, -7.0), (-3.464101615137755, -1.0)],
        [(-1.7320508075688772, 2.0), (-1.7320508075688772, 7.0), (0.0, 9.0), (3.464101615137755, 7.0), (3.464101615137755, 2.0), (0.0, -1.0), (-1.7320508075688772, 2.0)],
        [(1.7320508075688772, 5.0), (1.7320508075688772, 10.0), (3.4641016151377553, 12.0), (6.92820323027551, 10.0), (6.92820323027551, 5.0), (3.4641016151377553, 2.0), (1.7320508075688772, 5.0)]
    ]
    assert result == expected

def test_calculate_polygons_narrow_vertical_area_radius_1():
    result = calculate_polygons(startx=1, starty=1, endx=1.5, endy=4, radius=1)
    expected = [
        [(-0.7320508075688774, 0.5), (-0.7320508075688774, 2.5), (0.1349745962155614, 4.0), (0.8660254037844387, 2.5), (0.8660254037844387, 0.5), (0.1349745962155614, -1.0), (-0.7320508075688774, 0.5)],
        [(0.1349745962155614, 3.0), (0.1349745962155614, 5.0), (0.8660254037844387, 6.5), (1.7320508075688774, 5.0), (1.7320508075688774, 3.0), (0.8660254037844387, 0.5), (0.1349745962155614, 3.0)]
    ]
    assert result == expected

def test_calculate_polygons_single_point_radius_0_5():
    result = calculate_polygons(startx=0, starty=0, endx=0, endy=0, radius=0.5)
    expected = [
        [(-0.8660254037844386, -0.25), (-0.8660254037844386, 0.75), (-0.4330127018922193, 1.5), (0.43301270189221935, 0.75), (0.43301270189221935, -0.25), (-0.4330127018922193, -1.25), (-0.8660254037844386, -0.25)]
    ]
    assert result == expected