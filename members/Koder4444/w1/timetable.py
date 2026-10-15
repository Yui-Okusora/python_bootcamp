def by_day(courses: list[tuple[str, str]]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}

    for course, day in courses:
        if day not in result:
            result[day] = []
        result[day].append(course)

    for course_list in result.items():
        course_list.sort()
    return result
