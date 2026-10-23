import re
from datetime import date, timedelta


def parse_due(text: str, today: date) -> date:
    """Chuyển đổi chuỗi văn bản mô tả ngày thành đối tượng ngày cụ thể dựa trên ngày mốc."""
    text = text.lower().strip()
    
    if text == "tomorrow":
        return today + timedelta(days=1)
        
    try:
        return date.fromisoformat(text)
    except ValueError:
        pass
        
    match_days = re.match(r"in\s+(\d+)\s+days?", text)
    if match_days:
        days = int(match_days.group(1))
        return today + timedelta(days=days)
        
    weekdays = {
        "mon": 0, "tue": 1, "wed": 2, "thu": 3, "fri": 4, "sat": 5, "sun": 6
    }
    prefix = text[:3]
    if prefix in weekdays:
        target_idx = weekdays[prefix]
        current_idx = today.weekday()
        days_ahead = target_idx - current_idx
        if days_ahead <= 0:
            days_ahead += 7
        return today + timedelta(days=days_ahead)
        
    raise ValueError(f"Unknown date format: {text}")