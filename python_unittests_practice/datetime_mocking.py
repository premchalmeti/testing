from unittest.mock import Mock

# mock datetime libary to test is_weekday()

def is_weekday():
    today = datetime.datetime.today()

    return (0 <= today.weekday() < 5)


import datetime as dt

tuesday = dt.date(year=2019, month=1, day=1)
saturday = dt.date(year=2019, month=1, day=5)


datetime = Mock()

datetime.datetime.today.return_value = tuesday
assert is_weekday()


datetime.datetime.today.return_value = saturday
assert not is_weekday()
