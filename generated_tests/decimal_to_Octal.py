def decimal_to_Octal(deciNum):
    octalNum = 0
    countval = 1;
    dNo = deciNum;
    while (deciNum!= 0):
        remainder= deciNum % 8;
        octalNum+= remainder*countval;
        countval= countval*10;
        deciNum //= 8; 
    return (octalNum)

import pytest

def test_convert_zero_to_octal():
    # Input is zero, the while loop does not execute, so octalNum remains 0.
    assert decimal_to_Octal(0) == 0

def test_convert_small_decimal_less_than_8():
    # 5 % 8 = 5, octalNum = 5 * 1 = 5, deciNum //= 8 becomes 0, loop ends, output is 5.
    assert decimal_to_Octal(5) == 5

def test_convert_decimal_8_to_octal():
    # 8 % 8 = 0, octalNum = 0 * 1 = 0, deciNum //= 8 = 1; next iteration: 1 % 8 = 1, octalNum += 1 * 10 = 10, deciNum //= 8 = 0; loop ends, output is 10.
    assert decimal_to_Octal(8) == 10

def test_convert_decimal_64_to_octal():
    # 64 % 8 = 0, octalNum = 0 * 1 = 0, deciNum //= 8 = 8; next iteration: 8 % 8 = 0, octalNum += 0 * 10 = 0, countval=100, deciNum //= 8 = 1; next iteration: 1 % 8 = 1, octalNum += 1 * 100 = 100, deciNum //= 8 = 0; loop ends, output is 100.
    assert decimal_to_Octal(64) == 100

def test_convert_decimal_83_to_octal():
    # 83 % 8 = 3, octalNum = 3 * 1 = 3, deciNum //= 8 = 10; next iteration: 10 % 8 = 2, octalNum += 2 * 10 = 23, countval=100, deciNum //= 8 = 1; next iteration: 1 % 8 = 1, octalNum += 1 * 100 = 123, deciNum //= 8 = 0; loop ends, output is 123.
    assert decimal_to_Octal(83) == 123

def test_convert_decimal_255_to_octal():
    # 255 % 8 = 7, octalNum = 7 * 1 = 7, deciNum //= 8 = 31; next iteration: 31 % 8 = 7, octalNum += 7 * 10 = 77, countval=100, deciNum //= 8 = 3; next iteration: 3 % 8 = 3, octalNum += 3 * 100 = 377, deciNum //= 8 = 0; loop ends, output is 377.
    assert decimal_to_Octal(255) == 377