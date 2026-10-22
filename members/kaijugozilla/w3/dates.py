import re
from datetime import date, timedelta

WEEKDAYS = {
    "mon": 0, "monday": 0,
    "tue": 1, "tuesday": 1,
    "wed": 2, "wednesday": 2,
    "thu": 3, "thursday": 3,
    "fri": 4, "friday": 4,
    "sat": 5, "saturday": 5,
    "sun": 6, "sunday": 6,
}


def parse_due(text: str, today: date) -> date:
    """Convert date expressions into a date."""
  
    value = text.strip().lower()

    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        try:
            return date.fromisoformat(value)
        except ValueError as error:
            raise ValueError(f"Invalid date: {text}") from error

    if value == "tomorrow":
        return today + timedelta(days=1)

    match = re.fullmatch(r"in (\d+) days?", value)
    if match:
        return today + timedelta(days=int(match.group(1)))

    if value in WEEKDAYS:
        distance = (WEEKDAYS[value] - today.weekday()) % 7
        if distance == 0:
            distance = 7
        return today + timedelta(days=distance)

    raise ValueError(f"Unknown due date: {text}")
