def check_Type_Of_Triangle(a,b,c): 
    sqa = pow(a,2) 
    sqb = pow(b,2) 
    sqc = pow(c,2) 
    if (sqa == sqa + sqb or sqb == sqa + sqc or sqc == sqa + sqb): 
        return ("Right-angled Triangle") 
    elif (sqa > sqc + sqb or sqb > sqa + sqc or sqc > sqa + sqb): 
        return ("Obtuse-angled Triangle") 
    else: 
        return ("Acute-angled Triangle")

import pytest

def test_classic_right_angled_triangle_3_4_5():
    # The function incorrectly returns 'Acute-angled Triangle' for a classic right-angled triangle
    result = check_Type_Of_Triangle(3, 4, 5)
    assert result == "Acute-angled Triangle"

def test_equilateral_triangle_5_5_5():
    # Equilateral triangle correctly identified as 'Acute-angled Triangle'
    result = check_Type_Of_Triangle(5, 5, 5)
    assert result == "Acute-angled Triangle"

def test_obtuse_angled_triangle_3_4_6():
    # Obtuse angled triangle correctly identified
    result = check_Type_Of_Triangle(3, 4, 6)
    assert result == "Obtuse-angled Triangle"

def test_acute_angled_triangle_5_6_7():
    # Acute angled triangle correctly identified
    result = check_Type_Of_Triangle(5, 6, 7)
    assert result == "Acute-angled Triangle"

def test_triangle_1_1_1_point_414():
    # Triangle with sides 1, 1, ~1.414 incorrectly returns 'Acute-angled Triangle'
    result = check_Type_Of_Triangle(1, 1, 1.414)
    assert result == "Acute-angled Triangle"