def find_Points(l1,r1,l2,r2): 
    x = min(l1,l2) if (l1 != l2) else -1
    y = max(r1,r2) if (r1 != r2) else -1
    return (x,y)

import pytest

def test_different_left_and_right_endpoints():
    # Different left endpoints and different right endpoints
    result = find_Points(l1=1, r1=3, l2=2, r2=4)
    assert result == (1, 4)

def test_same_left_endpoints_different_right_endpoints():
    # Same left endpoints and different right endpoints
    result = find_Points(l1=5, r1=7, l2=5, r2=10)
    assert result == (-1, 10)

def test_different_left_endpoints_same_right_endpoints():
    # Different left endpoints and same right endpoints
    result = find_Points(l1=3, r1=8, l2=1, r2=8)
    assert result == (1, -1)

def test_same_left_and_right_endpoints():
    # Same left endpoints and same right endpoints
    result = find_Points(l1=4, r1=6, l2=4, r2=6)
    assert result == (-1, -1)

def test_left_and_right_endpoints_differ_with_negative_values():
    # Left endpoints differ, right endpoints differ with negative values
    result = find_Points(l1=-3, r1=-1, l2=-5, r2=-2)
    assert result == (-5, -1)