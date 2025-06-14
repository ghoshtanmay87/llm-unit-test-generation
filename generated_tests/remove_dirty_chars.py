NO_OF_CHARS = 256
def str_to_list(string): 
	temp = [] 
	for x in string: 
		temp.append(x) 
	return temp 
def lst_to_string(List): 
	return ''.join(List) 
def get_char_count_array(string): 
	count = [0] * NO_OF_CHARS 
	for i in string: 
		count[ord(i)] += 1
	return count 
def remove_dirty_chars(string, second_string): 
	count = get_char_count_array(second_string) 
	ip_ind = 0
	res_ind = 0
	temp = '' 
	str_list = str_to_list(string) 
	while ip_ind != len(str_list): 
		temp = str_list[ip_ind] 
		if count[ord(temp)] == 0: 
			str_list[res_ind] = str_list[ip_ind] 
			res_ind += 1
		ip_ind+=1
	return lst_to_string(str_list[0:res_ind])

import pytest

def test_remove_characters_from_first_string_that_appear_in_second_string():
    input_string = 'hello world'
    second_string = 'aeiou'
    expected_output = 'hll wrld'
    assert remove_dirty_chars(input_string, second_string) == expected_output

def test_no_characters_removed_when_second_string_is_empty():
    input_string = 'test string'
    second_string = ''
    expected_output = 'test string'
    assert remove_dirty_chars(input_string, second_string) == expected_output

def test_all_characters_removed_when_second_string_contains_all_characters_of_first_string():
    input_string = 'abc'
    second_string = 'abc'
    expected_output = ''
    assert remove_dirty_chars(input_string, second_string) == expected_output

def test_remove_digits_from_string():
    input_string = 'a1b2c3'
    second_string = '123'
    expected_output = 'abc'
    assert remove_dirty_chars(input_string, second_string) == expected_output

def test_remove_special_characters_from_string():
    input_string = 'hello!@#'
    second_string = '!@#'
    expected_output = 'hello'
    assert remove_dirty_chars(input_string, second_string) == expected_output

def test_remove_spaces_from_string():
    input_string = 'a b c d e'
    second_string = ' '
    expected_output = 'abcde'
    assert remove_dirty_chars(input_string, second_string) == expected_output

def test_case_sensitive_removal_only_exact_case_characters_removed():
    input_string = 'AbcABCabc'
    second_string = 'aC'
    expected_output = 'AbABcb'
    assert remove_dirty_chars(input_string, second_string) == expected_output

def test_empty_input_string_returns_empty_output():
    input_string = ''
    second_string = 'abc'
    expected_output = ''
    assert remove_dirty_chars(input_string, second_string) == expected_output

def test_second_string_with_repeated_characters_does_not_affect_removal():
    input_string = 'banana'
    second_string = 'aa'
    expected_output = 'bnn'
    assert remove_dirty_chars(input_string, second_string) == expected_output

def test_remove_newline_and_tab_characters_from_string():
    input_string = 'line1\nline2\tend'
    second_string = '\n\t'
    expected_output = 'line1line2end'
    assert remove_dirty_chars(input_string, second_string) == expected_output