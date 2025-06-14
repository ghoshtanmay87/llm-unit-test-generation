def get_Min_Squares(n):
    if n <= 3:
        return n;
    res = n 
    for x in range(1,n + 1):
        temp = x * x;
        if temp > n:
            break
        else:
            res = min(res,1 + get_Min_Squares(n  - temp)) 
    return res;

import pytest

def test_min_squares_n_0_edge_case():
    # Since n=0, no squares are needed, so the function returns 0 immediately.
    assert get_Min_Squares(0) == 0

def test_min_squares_n_1_base_case():
    # For n=1, the function returns 1 directly because 1 is a perfect square itself.
    assert get_Min_Squares(1) == 1

def test_min_squares_n_2_base_case():
    # For n=2, the function returns 2 because 2 = 1^2 + 1^2, and no fewer squares can sum to 2.
    assert get_Min_Squares(2) == 2

def test_min_squares_n_3_base_case():
    # For n=3, the function returns 3 because 3 = 1^2 + 1^2 + 1^2, and no fewer squares can sum to 3.
    assert get_Min_Squares(3) == 3

def test_min_squares_n_4_perfect_square():
    # 4 is a perfect square (2^2), so the minimum number of squares is 1.
    assert get_Min_Squares(4) == 1

def test_min_squares_n_5():
    # 5 = 4 (2^2) + 1 (1^2), so minimum squares needed is 2.
    assert get_Min_Squares(5) == 2

def test_min_squares_n_6():
    # 6 can be expressed as 4 + 1 + 1 (2^2 + 1^2 + 1^2), so minimum squares needed is 3.
    assert get_Min_Squares(6) == 3

def test_min_squares_n_7():
    # 7 = 4 + 1 + 1 + 1 (2^2 + 1^2 + 1^2 + 1^2), so minimum squares needed is 4.
    assert get_Min_Squares(7) == 4

def test_min_squares_n_8():
    # 8 = 4 + 4 (2^2 + 2^2), so minimum squares needed is 2.
    assert get_Min_Squares(8) == 2

def test_min_squares_n_9_perfect_square():
    # 9 is a perfect square (3^2), so the minimum number of squares is 1.
    assert get_Min_Squares(9) == 1

def test_min_squares_n_10():
    # 10 = 9 + 1 (3^2 + 1^2), so minimum squares needed is 2.
    assert get_Min_Squares(10) == 2

def test_min_squares_n_12():
    # 12 = 4 + 4 + 4 (2^2 + 2^2 + 2^2), so minimum squares needed is 3.
    assert get_Min_Squares(12) == 3

def test_min_squares_n_13():
    # 13 = 9 + 4 (3^2 + 2^2), so minimum squares needed is 2.
    assert get_Min_Squares(13) == 2