def is_triangleexists(a,b,c): 
    if(a != 0 and b != 0 and c != 0 and (a + b + c)== 180): 
        if((a + b)>= c or (b + c)>= a or (a + c)>= b): 
            return True 
        else:
            return False
    else:
        return False

import pytest

def test_all_angles_non_zero_and_sum_exactly_180():
    # All angles are non-zero and sum to 180.
    # The condition (a + b) >= c or (b + c) >= a or (a + c) >= b is True since 60+60=120 >= 60.
    # Hence, returns True.
    assert is_triangleexists(60, 60, 60) is True

def test_one_angle_is_zero():
    # One angle is zero, so the first condition a != 0 and b != 0 and c != 0 fails,
    # returning False immediately.
    assert is_triangleexists(0, 90, 90) is False

def test_sum_of_angles_not_equal_to_180():
    # Sum of angles is 150, not 180, so the function returns False.
    assert is_triangleexists(50, 50, 50) is False

def test_sum_180_but_one_angle_zero():
    # Even though sum is 180, one angle is zero, so returns False.
    assert is_triangleexists(0, 90, 90) is False

def test_sum_180_but_some_sums_less_than_third_angle():
    # All angles non-zero and sum to 180.
    # Check (a + b) >= c: 10+20=30 < 150 (False),
    # (b + c) >= a: 20+150=170 >= 10 (True),
    # (a + c) >= b: 10+150=160 >= 20 (True).
    # Since at least one condition is True, returns True.
    assert is_triangleexists(10, 20, 150) is True

def test_sum_180_all_sums_greater_than_third_angle():
    # Sum is 180, all angles non-zero.
    # Check sums: (a + b)=140 >= c=40 (True), so returns True.
    assert is_triangleexists(100, 40, 40) is True

def test_all_angles_non_zero_sum_180_borderline_sums():
    # Sum is 180, all non-zero.
    # (a + b)=135 >= c=45 (True), so returns True.
    assert is_triangleexists(90, 45, 45) is True

def test_all_angles_non_zero_sum_180_sums_pass():
    # Sum is 180, all non-zero.
    # (a + b)=130 >= c=50 (True), so returns True.
    assert is_triangleexists(70, 60, 50) is True

def test_all_angles_non_zero_sum_180_sums_fail_but_others_pass():
    # Sum is 180, all non-zero.
    # (a + b)=2 < c=178 (False),
    # (b + c)=179 >= a=1 (True),
    # (a + c)=179 >= b=1 (True).
    # Since at least one sum condition is True, returns True.
    assert is_triangleexists(1, 1, 178) is True