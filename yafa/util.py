import datetime


def parse_date_str(date_str: str) -> datetime.date:
    parsed_date = datetime.date.fromisoformat(date_str)
    return parsed_date
