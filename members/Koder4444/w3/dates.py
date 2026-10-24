import re
from datetime import date, timedelta


def parse_due(text: str, today: date) -> date:
    """Parse a date string (ISO format, relative days, or weekday) into a date object relative to today."""
    clean_text = text.strip().lower()

    try:
        return date.fromisoformat(clean_text)
    except ValueError:
        pass

    if clean_text == "today":
        return today
    if clean_text == "tomorrow":
        return today + timedelta(days=1)

    match_in_days = re.fullmatch(r"in\s+(\d+)\s+days?", clean_text)
    if match_in_days:
        days_offset = int(match_in_days.group(1))
        return today + timedelta(days=days_offset)

    weekdays = {
        "mon": 0, "monday": 0,
        "tue": 1, "tuesday": 1,
        "wed": 2, "wednesday": 2,
        "thu": 3, "thursday": 3,
        "fri": 4, "friday": 4,
        "sat": 5, "saturday": 5,
        "sun": 6, "sunday": 6,
    }

    if clean_text in weekdays:
        target_weekday = weekdays[clean_text]
        current_weekday = today.weekday()
        
        days_ahead = target_weekday - current_weekday
        if days_ahead <= 0:
            days_ahead += 7
            
        return today + timedelta(days=days_ahead)

    raise ValueError(f"Unknown date format: '{text}'")