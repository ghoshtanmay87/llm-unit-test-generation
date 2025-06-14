def rgb_to_hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = (df/mx)*100
    v = mx*100
    return h, s, v

import pytest

def test_convert_pure_red_to_hsv():
    # Convert pure red color to HSV
    r, g, b = 255, 0, 0
    expected = (0.0, 100.0, 100.0)
    assert rgb_to_hsv(r, g, b) == expected

def test_convert_pure_green_to_hsv():
    # Convert pure green color to HSV
    r, g, b = 0, 255, 0
    expected = (120.0, 100.0, 100.0)
    assert rgb_to_hsv(r, g, b) == expected

def test_convert_pure_blue_to_hsv():
    # Convert pure blue color to HSV
    r, g, b = 0, 0, 255
    expected = (240.0, 100.0, 100.0)
    assert rgb_to_hsv(r, g, b) == expected

def test_convert_black_to_hsv():
    # Convert black color to HSV
    r, g, b = 0, 0, 0
    expected = (0, 0, 0)
    assert rgb_to_hsv(r, g, b) == expected

def test_convert_white_to_hsv():
    # Convert white color to HSV
    r, g, b = 255, 255, 255
    expected = (0, 0, 100.0)
    assert rgb_to_hsv(r, g, b) == expected

def test_convert_gray_128_128_128_to_hsv():
    # Convert gray color (128, 128, 128) to HSV
    r, g, b = 128, 128, 128
    expected = (0, 0, 50.19607843137255)
    assert rgb_to_hsv(r, g, b) == expected

def test_convert_color_75_0_130_to_hsv():
    # Convert color (75, 0, 130) to HSV
    r, g, b = 75, 0, 130
    expected = (274.6153846153846, 100.0, 50.98039215686274)
    assert rgb_to_hsv(r, g, b) == expected

def test_convert_yellow_255_255_0_to_hsv():
    # Convert color (255, 255, 0) (yellow) to HSV
    r, g, b = 255, 255, 0
    expected = (60.0, 100.0, 100.0)
    assert rgb_to_hsv(r, g, b) == expected

def test_convert_cyan_0_255_255_to_hsv():
    # Convert color (0, 255, 255) (cyan) to HSV
    r, g, b = 0, 255, 255
    expected = (180.0, 100.0, 100.0)
    assert rgb_to_hsv(r, g, b) == expected

def test_convert_magenta_255_0_255_to_hsv():
    # Convert color (255, 0, 255) (magenta) to HSV
    r, g, b = 255, 0, 255
    expected = (300.0, 100.0, 100.0)
    assert rgb_to_hsv(r, g, b) == expected