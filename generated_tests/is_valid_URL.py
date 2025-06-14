import re
def is_valid_URL(str):
	regex = ("((http|https)://)(www.)?" +
			"[a-zA-Z0-9@:%._\+~#?&//=]" +
			"{2,256}\.[a-z]" +
			"{2,6}\b([-a-zA-Z0-9@:%" +
			"._\+~#?&//=]*)")
	p = re.compile(regex)
	if (str == None):
		return False
	if(re.search(p, str)):
		return True
	else:
		return False

import pytest

def test_valid_http_url_with_www_prefix():
    input_str = 'http://www.example.com'
    expected = True
    assert is_valid_URL(input_str) == expected

def test_valid_https_url_without_www_prefix():
    input_str = 'https://example.org'
    expected = True
    assert is_valid_URL(input_str) == expected

def test_url_missing_protocol():
    input_str = 'www.example.com'
    expected = False
    assert is_valid_URL(input_str) == expected

def test_url_with_invalid_tld_length():
    input_str = 'http://example.c'
    expected = False
    assert is_valid_URL(input_str) == expected

def test_url_with_subdomain_and_path():
    input_str = 'https://sub.domain-example.com/path/to/page'
    expected = True
    assert is_valid_URL(input_str) == expected

def test_none_input():
    input_str = None
    expected = False
    assert is_valid_URL(input_str) == expected

def test_url_with_port_number():
    input_str = 'http://example.com:8080'
    expected = True
    assert is_valid_URL(input_str) == expected

def test_url_with_query_parameters():
    input_str = 'https://example.com?query=123&sort=asc'
    expected = True
    assert is_valid_URL(input_str) == expected

def test_url_with_invalid_characters_in_domain():
    input_str = 'http://exa mple.com'
    expected = False
    assert is_valid_URL(input_str) == expected

def test_url_with_uppercase_tld():
    input_str = 'http://example.COM'
    expected = False
    assert is_valid_URL(input_str) == expected