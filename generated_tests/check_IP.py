import re 
regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
			25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
			25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
			25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''
def check_IP(Ip): 
	if(re.search(regex, Ip)): 
		return ("Valid IP address") 
	else: 
		return ("Invalid IP address")

import pytest

def test_valid_ip_all_octets_in_range():
    # Each octet (192, 168, 1, 1) is within 0-255, matching the regex pattern for valid IPv4 addresses.
    input_ip = '192.168.1.1'
    expected = 'Valid IP address'
    assert check_IP(input_ip) == expected

def test_invalid_ip_octet_exceeds_255():
    # The first octet is 256, which is outside the valid range 0-255, so it does not match the regex.
    input_ip = '256.100.50.25'
    expected = 'Invalid IP address'
    assert check_IP(input_ip) == expected

def test_invalid_ip_negative_octet():
    # Negative numbers are not allowed in IP addresses and the regex does not match a leading '-' sign.
    input_ip = '-1.100.100.100'
    expected = 'Invalid IP address'
    assert check_IP(input_ip) == expected

def test_valid_ip_single_digit_octets():
    # All octets are single digits within 0-9, which is valid and matches the regex.
    input_ip = '1.2.3.4'
    expected = 'Valid IP address'
    assert check_IP(input_ip) == expected

def test_invalid_ip_missing_octet():
    # Only three octets are present instead of four, so the regex does not match.
    input_ip = '192.168.1'
    expected = 'Invalid IP address'
    assert check_IP(input_ip) == expected

def test_invalid_ip_extra_octet():
    # Five octets are present instead of four, so the regex does not match.
    input_ip = '192.168.1.1.1'
    expected = 'Invalid IP address'
    assert check_IP(input_ip) == expected

def test_valid_ip_leading_zeros_in_octets():
    # Leading zeros are allowed by the regex as it matches optional leading zeros in each octet, and values are within 0-255.
    input_ip = '001.002.003.004'
    expected = 'Valid IP address'
    assert check_IP(input_ip) == expected

def test_invalid_ip_non_numeric_characters():
    # The second octet contains non-numeric characters 'abc', which does not match the regex.
    input_ip = '192.abc.1.1'
    expected = 'Invalid IP address'
    assert check_IP(input_ip) == expected

def test_valid_ip_octet_zero():
    # All octets are zero, which is valid and matches the regex.
    input_ip = '0.0.0.0'
    expected = 'Valid IP address'
    assert check_IP(input_ip) == expected

def test_valid_ip_octet_255():
    # All octets are 255, the maximum allowed value, matching the regex.
    input_ip = '255.255.255.255'
    expected = 'Valid IP address'
    assert check_IP(input_ip) == expected