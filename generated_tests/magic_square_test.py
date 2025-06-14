def magic_square_test(my_matrix):
    iSize = len(my_matrix[0])
    sum_list = []
    sum_list.extend([sum (lines) for lines in my_matrix])   
    for col in range(iSize):
        sum_list.append(sum(row[col] for row in my_matrix))
    result1 = 0
    for i in range(0,iSize):
        result1 +=my_matrix[i][i]
    sum_list.append(result1)      
    result2 = 0
    for i in range(iSize-1,-1,-1):
        result2 +=my_matrix[i][i]
    sum_list.append(result2)
    if len(set(sum_list))>1:
        return False
    return True

import pytest

def test_magic_square_3x3_true():
    my_matrix = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
    expected = True
    assert magic_square_test(my_matrix) == expected

def test_non_magic_square_3x3_different_row_sums():
    my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected = False
    assert magic_square_test(my_matrix) == expected

def test_non_magic_square_2x2():
    my_matrix = [[1, 2], [3, 4]]
    expected = False
    assert magic_square_test(my_matrix) == expected

def test_magic_square_1x1_trivial():
    my_matrix = [[7]]
    expected = True
    assert magic_square_test(my_matrix) == expected

def test_magic_square_4x4_true():
    my_matrix = [[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 7, 12], [4, 15, 14, 1]]
    expected = True
    assert magic_square_test(my_matrix) == expected

def test_non_magic_square_4x4_diagonal_mismatch():
    my_matrix = [[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 7, 12], [4, 15, 14, 2]]
    expected = False
    assert magic_square_test(my_matrix) == expected