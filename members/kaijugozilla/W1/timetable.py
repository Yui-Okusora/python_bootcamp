def by_day(items: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Group courses by day and sort the courses alphabetically."""
    timetable = {}

    for course, day in items:
        timetable.setdefault(day, []).append(course)

    for day, courses in timetable.items():
        courses.sort()

    return timetable
