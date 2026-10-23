"""Module xử lý và phân tích chuỗi văn bản thành ngày tháng (Date parsing)."""

import re
from datetime import date, timedelta


def parse_due(text: str, today: date) -> date:
    """Chuyển đổi các định dạng chuỗi mô tả thời gian thành đối tượng date.

    Args:
        text (str): Chuỗi ngày tháng (vd: 'tomorrow', 'in 3 days', 'mon', 'YYYY-MM-DD').
        today (date): Ngày mốc để tính toán.

    Returns:
        date: Đối tượng ngày đã được tính toán.

    Raises:
        ValueError: Nếu định dạng chuỗi không hợp lệ.
    """
    text = text.lower().strip()

    if text == "tomorrow":
        return today + timedelta(days=1)

    match_days = re.match(r"in (\d+) days?", text)
    if match_days:
        days = int(match_days.group(1))
        return today + timedelta(days=days)

    weekdays = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    if text in weekdays:
        target_weekday = weekdays.index(text)
        current_weekday = today.weekday()
        days_ahead = target_weekday - current_weekday
        if days_ahead <= 0:
            days_ahead += 7
        return today + timedelta(days=days_ahead)

    try:
        return date.fromisoformat(text)
    except ValueError as exc:
        raise ValueError(f"Unknown date format: {text}") from exc