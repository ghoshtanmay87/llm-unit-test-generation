def file_name_check(file_name):
    suf = ['txt', 'exe', 'dll']
    lst = file_name.split(sep='.')
    if len(lst) != 2:
        return 'No'
    if not lst[1] in suf:
        return 'No'
    if len(lst[0]) == 0:
        return 'No'
    if not lst[0][0].isalpha():
        return 'No'
    t = len([x for x in lst[0] if x.isdigit()])
    if t > 3:
        return 'No'
    return 'Yes'

import pytest

def test_valid_file_name_with_allowed_suffix_and_valid_conditions():
    # Splitting 'file123.txt' by '.' gives ['file123', 'txt']. Length is 2, suffix 'txt' is allowed,
    # base 'file123' is non-empty, starts with 'f' (alpha), digits count is 3 (123) which is not more than 3,
    # so returns 'Yes'.
    assert file_name_check('file123.txt') == 'Yes'

def test_file_name_with_no_suffix_separator():
    # Splitting 'filetxt' by '.' gives ['filetxt'], length is 1, not 2, so returns 'No'.
    assert file_name_check('filetxt') == 'No'

def test_file_name_with_multiple_dots():
    # Splitting 'file.name.txt' by '.' gives ['file', 'name', 'txt'], length is 3, not 2, so returns 'No'.
    assert file_name_check('file.name.txt') == 'No'

def test_file_name_with_disallowed_suffix():
    # Splitting 'file123.pdf' by '.' gives ['file123', 'pdf'], suffix 'pdf' not in ['txt', 'exe', 'dll'], so returns 'No'.
    assert file_name_check('file123.pdf') == 'No'

def test_file_name_with_empty_base_name():
    # Splitting '.txt' by '.' gives ['', 'txt'], base name is empty string, so returns 'No'.
    assert file_name_check('.txt') == 'No'

def test_file_name_base_does_not_start_with_alphabet():
    # Splitting '1file.txt' by '.' gives ['1file', 'txt'], base starts with '1' which is not alphabetic, so returns 'No'.
    assert file_name_check('1file.txt') == 'No'

def test_file_name_with_more_than_3_digits_in_base():
    # Splitting 'file1234.txt' by '.' gives ['file1234', 'txt'], digits in base are '1','2','3','4' (4 digits),
    # which is more than 3, so returns 'No'.
    assert file_name_check('file1234.txt') == 'No'

def test_file_name_with_exactly_3_digits_in_base():
    # Splitting 'f12g3.exe' by '.' gives ['f12g3', 'exe'], suffix allowed, base starts with 'f' (alpha),
    # digits are '1','2','3' (3 digits), not more than 3, so returns 'Yes'.
    assert file_name_check('f12g3.exe') == 'Yes'

def test_file_name_with_zero_digits_in_base():
    # Splitting 'filename.dll' by '.' gives ['filename', 'dll'], suffix allowed, base starts with 'f' (alpha),
    # digits count is 0, so returns 'Yes'.
    assert file_name_check('filename.dll') == 'Yes'

def test_file_name_with_suffix_in_uppercase_case_sensitive_check():
    # Splitting 'file123.TXT' by '.' gives ['file123', 'TXT'], suffix 'TXT' is uppercase and not in ['txt', 'exe', 'dll'] (case sensitive),
    # so returns 'No'.
    assert file_name_check('file123.TXT') == 'No'