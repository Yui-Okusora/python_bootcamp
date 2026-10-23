from datetime import date, timedelta
import re

def parse_due(text: str, today: date) -> date:
    """Phân tích chuỗi thời gian thành đối tượng datetime.date."""
    text = text.strip()

    try:
        return date.fromisoformat(text)
    except ValueError:
        pass

    if text.lower() == "tomorrow":
        return today + timedelta(days=1)

    match = re.match(r"^in\s+(\d+)\s+days?$", text, re.IGNORECASE)
    if match:
        days = int(match.group(1))
        return today + timedelta(days=days)

    weekdays = {
        "mon" : 0, "monday" : 0,
        "tue" : 1, "tueday" : 1,
        "wed" : 2, "wednesday" : 2,
        "thu" : 3, "thursday" : 3,
        "fri" : 4, "friday" : 4,
        "sat" : 5, "saturday" : 5,
        "sun" : 6, "sunday": 6
    }

    target_wd = weekdays.get(text.lower())
    if target_wd is not None:
        days_ahead = (target_wd - today.weekday()) % 7
        if days_ahead == 0:
            days_ahead = 7
        return today + timedelta(days=days_ahead)

    raise ValueError(f"Unknown date format: '{text}'")