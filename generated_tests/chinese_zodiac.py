def chinese_zodiac(year):
 if (year - 2000) % 12 == 0:
     sign = 'Dragon'
 elif (year - 2000) % 12 == 1:
     sign = 'Snake'
 elif (year - 2000) % 12 == 2:
     sign = 'Horse'
 elif (year - 2000) % 12 == 3:
     sign = 'sheep'
 elif (year - 2000) % 12 == 4:
     sign = 'Monkey'
 elif (year - 2000) % 12 == 5:
     sign = 'Rooster'
 elif (year - 2000) % 12 == 6:
     sign = 'Dog'
 elif (year - 2000) % 12 == 7:
     sign = 'Pig'
 elif (year - 2000) % 12 == 8:
     sign = 'Rat'
 elif (year - 2000) % 12 == 9:
     sign = 'Ox'
 elif (year - 2000) % 12 == 10:
     sign = 'Tiger'
 else:
     sign = 'Hare'
 return sign

import pytest

def test_year_2000_base_year_dragon():
    # Year exactly 2000, base year for calculation
    year = 2000
    expected = "Dragon"
    assert chinese_zodiac(year) == expected

def test_year_2001_one_year_after_base_snake():
    # Year 2001, one year after base year
    year = 2001
    expected = "Snake"
    assert chinese_zodiac(year) == expected

def test_year_2011_eleven_years_after_base_hare():
    # Year 2011, eleven years after base year
    year = 2011
    expected = "Hare"
    assert chinese_zodiac(year) == expected

def test_year_1999_one_year_before_base_hare():
    # Year 1999, one year before base year
    year = 1999
    expected = "Hare"
    assert chinese_zodiac(year) == expected

def test_year_1988_twelve_years_before_base_dragon():
    # Year 1988, twelve years before base year
    year = 1988
    expected = "Dragon"
    assert chinese_zodiac(year) == expected

def test_year_2024_twenty_four_years_after_base_dragon():
    # Year 2024, twenty-four years after base year
    year = 2024
    expected = "Dragon"
    assert chinese_zodiac(year) == expected

def test_year_2003_three_years_after_base_sheep():
    # Year 2003, three years after base year
    year = 2003
    expected = "sheep"
    assert chinese_zodiac(year) == expected

def test_year_2010_ten_years_after_base_tiger():
    # Year 2010, ten years after base year
    year = 2010
    expected = "Tiger"
    assert chinese_zodiac(year) == expected

def test_year_2008_eight_years_after_base_rat():
    # Year 2008, eight years after base year
    year = 2008
    expected = "Rat"
    assert chinese_zodiac(year) == expected

def test_year_1995_five_years_before_base_pig():
    # Year 1995, five years before base year
    year = 1995
    expected = "Pig"
    assert chinese_zodiac(year) == expected