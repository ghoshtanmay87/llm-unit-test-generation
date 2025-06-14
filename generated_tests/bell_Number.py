def bell_Number(n): 
    bell = [[0 for i in range(n+1)] for j in range(n+1)] 
    bell[0][0] = 1
    for i in range(1, n+1):
        bell[i][0] = bell[i-1][i-1]
        for j in range(1, i+1): 
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1] 
    return bell[n][0]

import pytest

def test_bell_number_n_0_base_case():
    # For n=0, the function initializes bell[0][0] = 1 and returns bell[0][0], which is 1.
    assert bell_Number(0) == 1

def test_bell_number_n_1():
    # For n=1, bell[1][0] = bell[0][0] = 1, and bell[1][1] = bell[0][0] + bell[1][0] = 1 + 1 = 2,
    # but the function returns bell[1][0] = 1.
    assert bell_Number(1) == 1

def test_bell_number_n_2():
    # For n=2, bell[2][0] = bell[1][1] = 2, so the function returns 2.
    assert bell_Number(2) == 2

def test_bell_number_n_3():
    # For n=3, bell[3][0] = bell[2][2] = 5, so the function returns 5.
    assert bell_Number(3) == 5

def test_bell_number_n_4():
    # For n=4, bell[4][0] = bell[3][3] = 15, so the function returns 15.
    assert bell_Number(4) == 15

def test_bell_number_n_5():
    # For n=5, bell[5][0] = bell[4][4] = 52, so the function returns 52.
    assert bell_Number(5) == 52