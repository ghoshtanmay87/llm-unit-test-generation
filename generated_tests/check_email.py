import re 
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
def check_email(email): 
	if(re.search(regex,email)): 
		return ("Valid Email") 
	else: 
		return ("Invalid Email")

import pytest

def test_valid_email_lowercase_single_dot_before_domain():
    email = 'user.name@example.com'
    expected = 'Valid Email'
    assert check_email(email) == expected

def test_valid_email_lowercase_letters_digits_no_dot_or_underscore():
    email = 'username123@example.com'
    expected = 'Valid Email'
    assert check_email(email) == expected

def test_invalid_email_with_uppercase_letters():
    email = 'User.Name@example.com'
    expected = 'Invalid Email'
    assert check_email(email) == expected

def test_invalid_email_multiple_dots_before_at():
    email = 'user..name@example.com'
    expected = 'Invalid Email'
    assert check_email(email) == expected

def test_invalid_email_missing_at_symbol():
    email = 'username.example.com'
    expected = 'Invalid Email'
    assert check_email(email) == expected

def test_invalid_email_domain_extension_longer_than_three():
    email = 'username@example.comm'
    expected = 'Invalid Email'
    assert check_email(email) == expected

def test_valid_email_with_underscore_in_local_part():
    email = 'user_name@example.com'
    expected = 'Valid Email'
    assert check_email(email) == expected

def test_invalid_email_with_special_character_in_local_part():
    email = 'user!name@example.com'
    expected = 'Invalid Email'
    assert check_email(email) == expected

def test_valid_email_with_digits_in_domain_name():
    email = 'username@exampl3.com'
    expected = 'Valid Email'
    assert check_email(email) == expected

def test_valid_email_with_underscore_in_domain_name():
    email = 'username@exam_ple.com'
    expected = 'Valid Email'
    assert check_email(email) == expected

def test_invalid_email_with_uppercase_letters_in_domain_extension():
    email = 'username@example.Com'
    expected = 'Invalid Email'
    assert check_email(email) == expected

def test_invalid_email_missing_domain_extension():
    email = 'username@example'
    expected = 'Invalid Email'
    assert check_email(email) == expected