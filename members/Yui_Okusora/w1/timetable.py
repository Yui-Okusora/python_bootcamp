def by_day(entries: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Group courses by day."""
    grouped: dict[str, list[str]] = {}

    for i in range(len(entries)):
        course, day = entries[i]
        if day not in grouped:
            grouped[day] = []
        grouped[day].append(course)

    result: dict[str, list[str]] = {}
    for day, courses in grouped.items():
        result[day] = sorted(courses)

    return result