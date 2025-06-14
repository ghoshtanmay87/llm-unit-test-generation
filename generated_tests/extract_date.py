import re
def extract_date(url):
        return re.findall(r'/(\d{4})/(\d{1,2})/(\d{1,2})/', url)

import pytest

def test_extract_date_standard_yyyy_mm_dd():
    # Extract date from URL with standard YYYY/MM/DD format
    url = 'https://example.com/2023/07/15/article'
    expected = [('2023', '07', '15')]
    assert extract_date(url) == expected

def test_extract_date_single_digit_month_day():
    # Extract date from URL with single-digit month and day
    url = 'https://example.com/2023/7/5/article'
    expected = [('2023', '7', '5')]
    assert extract_date(url) == expected

def test_extract_date_no_pattern():
    # No date pattern in URL
    url = 'https://example.com/article/2023-07-15'
    expected = []
    assert extract_date(url) == expected

def test_extract_date_multiple_patterns():
    # Multiple date patterns in URL
    url = 'https://example.com/2022/12/31/summary/2023/01/01/newyear'
    expected = [('2022', '12', '31'), ('2023', '01', '01')]
    assert extract_date(url) == expected

def test_extract_date_pattern_at_end_no_trailing_slash():
    # Date pattern at the end of URL without trailing slash
    url = 'https://example.com/2023/07/15'
    expected = []
    assert extract_date(url) == expected