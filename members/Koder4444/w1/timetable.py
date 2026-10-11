def by_day(courses):
    result = {}
    for course, day in courses:
        result.setdefault(day, []).append(course)
        
    for day, value in result.items():
        result[day].sort()
    return result