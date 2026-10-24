def by_day(courses: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Group courses by day of the week and sort course names alphabetically for each day."""
    result: dict[str, list[str]] = {}

    for course, day in courses:
        if day not in result:
            result[day] = []
        result[day].append(course)

    for course_list in result.values():
        course_list.sort()

    return result