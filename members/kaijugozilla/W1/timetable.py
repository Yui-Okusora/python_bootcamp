def by_day(items: list[tuple[str, str]]) -> dict[str, list[str]]:
    timetable = {}

    for course, day in items:
        timetable.setdefault(day, []).append(course)

    for day, courses in timetable.items():
        courses.sort()

    return timetable
