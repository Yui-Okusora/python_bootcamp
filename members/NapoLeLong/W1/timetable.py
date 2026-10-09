def by_day(schedule: list[tuple[str, str]]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for course, day in sorted(schedule):
        result.setdefault(day, []).append(course)
    return result