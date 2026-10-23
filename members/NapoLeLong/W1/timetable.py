def by_day(schedule: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Gom nhóm danh sách khóa học theo từng ngày trong tuần."""
    res: dict[str, list[str]] = {}
    for course, day in sorted(schedule):
        res.setdefault(day, []).append(course)
    return res