def courses_by_day_setdefault(schedule):
    grouped = {}
    for course, day in schedule:
        grouped.setdefault(day, []).append(course)
    
    return {day: sorted(courses) for day, courses in grouped.items()}

# Example usage
schedule = [("Math", "Mon"), ("Physics", "Mon"), ("Biology", "Tue"), ("Math", "Tue"), ("Art", "Mon")]
print(courses_by_day_setdefault(schedule))
