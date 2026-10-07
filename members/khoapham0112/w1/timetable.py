def by_day(courses):
    res = {}
    for course in courses:
        day = course[1]
        res.setdefault(day, [])
        res[day].append(course[0])
    for key in res:
        res[key].sort()
    return res

print(by_day([("CSC10014", "Mon"), ("MTH00003", "Tue"), ("CSC10001", "Mon")]))
