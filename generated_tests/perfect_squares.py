def perfect_squares(a, b):
    lists=[]
    for i in range (a,b+1):
        j = 1;
        while j*j <= i:
            if j*j == i:
                 lists.append(i)  
            j = j+1
        i = i+1
    return lists

import pytest

def test_range_includes_no_perfect_squares():
    # Numbers 2 and 3 are not perfect squares because 1*1=1 < 2 and 2*2=4 > 3, so no perfect squares in this range.
    result = perfect_squares(2, 3)
    assert result == []

def test_range_includes_one_perfect_square_at_start():
    # 1 is a perfect square (1*1=1), so it is included.
    result = perfect_squares(1, 1)
    assert result == [1]

def test_range_includes_multiple_perfect_squares():
    # Within 1 to 10, perfect squares are 1 (1*1), 4 (2*2), and 9 (3*3).
    result = perfect_squares(1, 10)
    assert result == [1, 4, 9]

def test_range_includes_perfect_squares_and_non_perfect_squares():
    # Between 10 and 20, only 16 (4*4) is a perfect square.
    result = perfect_squares(10, 20)
    assert result == [16]

def test_range_includes_single_perfect_square_at_end():
    # 16 is a perfect square (4*4), 15 is not.
    result = perfect_squares(15, 16)
    assert result == [16]

def test_range_includes_no_perfect_squares_with_larger_numbers():
    # No perfect squares between 26 and 30 because 5*5=25 < 26 and 6*6=36 > 30.
    result = perfect_squares(26, 30)
    assert result == []

def test_range_includes_multiple_perfect_squares_with_larger_numbers():
    # Between 20 and 40, perfect squares are 25 (5*5) and 36 (6*6).
    result = perfect_squares(20, 40)
    assert result == [25, 36]