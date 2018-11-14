import datetime

from yafa.util import parse_date_str


def test_parse_date_str_today():
    today = datetime.date.today()
    today_isoformat = today.isoformat()
    assert today == parse_date_str(today_isoformat)
