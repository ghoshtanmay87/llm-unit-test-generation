def month_season(month,days):
 if month in ('January', 'February', 'March'):
	 season = 'winter'
 elif month in ('April', 'May', 'June'):
	 season = 'spring'
 elif month in ('July', 'August', 'September'):
	 season = 'summer'
 else:
	 season = 'autumn'
 if (month == 'March') and (days > 19):
	 season = 'spring'
 elif (month == 'June') and (days > 20):
	 season = 'summer'
 elif (month == 'September') and (days > 21):
	 season = 'autumn'
 elif (month == 'October') and (days > 21):
	 season = 'autumn'
 elif (month == 'November') and (days > 21):
	 season = 'autumn'
 elif (month == 'December') and (days > 20):
	 season = 'winter'
 return season

import pytest

def test_month_january_any_day():
    # Month is January, any day
    result = month_season(month='January', days=15)
    assert result == 'winter'

def test_month_march_day_before_20():
    # Month is March, day before 20
    result = month_season(month='March', days=19)
    assert result == 'winter'

def test_month_march_day_after_19():
    # Month is March, day after 19
    result = month_season(month='March', days=20)
    assert result == 'spring'

def test_month_june_day_before_21():
    # Month is June, day before 21
    result = month_season(month='June', days=20)
    assert result == 'spring'

def test_month_june_day_after_20():
    # Month is June, day after 20
    result = month_season(month='June', days=21)
    assert result == 'summer'

def test_month_september_day_before_22():
    # Month is September, day before 22
    result = month_season(month='September', days=21)
    assert result == 'summer'

def test_month_september_day_after_21():
    # Month is September, day after 21
    result = month_season(month='September', days=22)
    assert result == 'autumn'

def test_month_october_day_before_22():
    # Month is October, day before 22
    result = month_season(month='October', days=21)
    assert result == 'autumn'

def test_month_october_day_after_21():
    # Month is October, day after 21
    result = month_season(month='October', days=22)
    assert result == 'autumn'

def test_month_november_day_before_22():
    # Month is November, day before 22
    result = month_season(month='November', days=21)
    assert result == 'autumn'

def test_month_november_day_after_21():
    # Month is November, day after 21
    result = month_season(month='November', days=22)
    assert result == 'autumn'

def test_month_december_day_before_21():
    # Month is December, day before 21
    result = month_season(month='December', days=20)
    assert result == 'autumn'

def test_month_december_day_after_20():
    # Month is December, day after 20
    result = month_season(month='December', days=21)
    assert result == 'winter'

def test_month_february_any_day():
    # Month is February, any day
    result = month_season(month='February', days=10)
    assert result == 'winter'

def test_month_may_any_day():
    # Month is May, any day
    result = month_season(month='May', days=15)
    assert result == 'spring'

def test_month_july_any_day():
    # Month is July, any day
    result = month_season(month='July', days=10)
    assert result == 'summer'

def test_month_august_any_day():
    # Month is August, any day
    result = month_season(month='August', days=31)
    assert result == 'summer'