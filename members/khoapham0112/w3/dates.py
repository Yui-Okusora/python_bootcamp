import re
from datetime import date, timedelta

"""return an exact date from the input date"""
def parse_due(text: str, today: date) -> date:
    s = text.strip().lower()

    if s == "tomorrow":
        return today + timedelta(days=1)

    if s == "today":
        return today

    match_in_days = re.fullmatch(r"in\s+(\d+)\s+days?", s)
    if match_in_days:
        return today + timedelta(days=int(match_in_days.group(1)))

    try:
        return date.fromisoformat(s)
    except ValueError:
        pass

    weekdays = {
        "mon": 0, "monday": 0,
        "tue": 1, "tues": 1, "tuesday": 1,
        "wed": 2, "wednesday": 2,
        "thu": 3, "thur": 3, "thurs": 3, "thursday": 3,
        "fri": 4, "friday": 4,
        "sat": 5, "saturday": 5,
        "sun": 6, "sunday": 6,
    }

    if s in weekdays:
        target_weekday = weekdays[s]
        days_ahead = (target_weekday - today.weekday() - 1) % 7 + 1
        return today + timedelta(days=days_ahead)

    raise ValueError(f"Unrecognized date expression: {text!r}")