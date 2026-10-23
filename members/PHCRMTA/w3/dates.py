import re
from datetime import date, timedelta

WEEKDAYS: dict[str, int] = {
    "mon": 0, "tue": 1, "wed": 2, "thu": 3, "fri": 4, "sat": 5, "sun": 6,
    "monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3,
    "friday": 4, "saturday": 5, "sunday": 6
}

def parse_due(text: str, today: date) -> date:
    """Parse a natural language date expression or ISO date string into a date object."""
    text_clean = text.strip().lower()

    # 1. ISO Format: "YYYY-MM-DD"
    try:
        return date.fromisoformat(text_clean)
    except ValueError:
        pass

    if text_clean == "today":
        return today
    if text_clean == "tomorrow":
        return today + timedelta(days=1)

    match = re.fullmatch(r"in\s+(\d+)\s+days?", text_clean)
    if match:
        days = int(match.group(1))
        return today + timedelta(days=days)

    if text_clean in WEEKDAYS:
        target_weekday = WEEKDAYS[text_clean]
        current_weekday = today.weekday()
        
        days_ahead = target_weekday - current_weekday
        if days_ahead <= 0: 
            days_ahead += 7
            
        return today + timedelta(days=days_ahead)

    raise ValueError(f"Unknown date format: '{text}'")