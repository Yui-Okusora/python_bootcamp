def by_day(pairs: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Group courses by day and return them sorted alphabetically per day."""
    result = {}

    for course, day in pairs:
        result.setdefault(day, []).append(course)

    for courses in result.values():
        courses.sort()

    return result