"""Module quản lý và sắp xếp lịch học theo từng ngày trong tuần."""


def courses_by_day_setdefault(
    schedule: list[tuple[str, str]],
) -> dict[str, list[str]]:
    """Gom nhóm và sắp xếp danh sách môn học theo từng ngày trong tuần.

    Args:
        schedule (list[tuple[str, str]]): Danh sách các cặp (tên_môn_học, ngày_học).

    Returns:
        dict[str, list[str]]: Tự điển với khóa là ngày và giá trị là danh sách các môn
            học đã sắp xếp theo thứ tự alphabet.
    """
    grouped: dict[str, list[str]] = {}
    for course, day in schedule:
        grouped.setdefault(day, []).append(course)

    return {day: sorted(courses) for day, courses in grouped.items()}


if __name__ == "__main__":
    schedule = [
        ("Math", "Mon"),
        ("Physics", "Mon"),
        ("Biology", "Tue"),
        ("Math", "Tue"),
        ("Art", "Mon"),
    ]
    print(courses_by_day_setdefault(schedule))