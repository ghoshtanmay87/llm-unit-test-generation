import re
def removezero_ip(ip):
 string = re.sub('\.[0]*', '.', ip)
 return string

import pytest

def test_remove_leading_zeros_from_each_octet():
    ip = '192.168.001.010'
    expected = '192.168.1.10'
    assert removezero_ip(ip) == expected

def test_ipv4_with_zeros_only_in_some_octets():
    ip = '10.0.0.1'
    expected = '10...1'
    assert removezero_ip(ip) == expected

def test_ipv4_with_no_zeros_after_dots():
    ip = '127.1.2.3'
    expected = '127.1.2.3'
    assert removezero_ip(ip) == expected

def test_ipv4_with_multiple_zeros_after_dots():
    ip = '0.00.000.0000'
    expected = '0...'
    assert removezero_ip(ip) == expected

def test_ipv4_with_zeros_in_middle_of_octets():
    ip = '192.168.100.010'
    expected = '192.168.100.10'
    assert removezero_ip(ip) == expected