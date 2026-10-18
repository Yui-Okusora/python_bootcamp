from datetime import date, timedelta

from shared.contract import Task
from shared.study_planner.prioritise import prioritise

"""Shared fixtures for the Python bootcamp tests.

Usage:
    python -m pytest shared/study_planner/test_prioritise.py
"""

def test_prioritise_basic_sorting():
    today = date(2026, 10, 1)

    task_a = Task(
        title="Task A",
        importance=5,
        effort_h=2.0,
        deadline=today + timedelta(days=5),
    )

    task_b = Task(
        title="Task B",
        importance=4,
        effort_h=1.5,
        deadline=today + timedelta(days=2),
    )

    result = prioritise([task_a, task_b], today)

    assert len(result) == 2
    assert result[0].title == "Task B"
    assert result[1].title == "Task A"


def test_prioritise_zero_or_negative_days_left():
    today = date(2026, 10, 1)

    task_today = Task(
        title="Today Task", importance=3, effort_h=1.0, deadline=today
    )

    task_overdue = Task(
        title="Overdue Task",
        importance=5,
        effort_h=2.0,
        deadline=today - timedelta(days=2),
    )

    result = prioritise([task_today, task_overdue], today)
    assert result[0].title == "Overdue Task"


def test_prioritise_empty_list():
    today = date(2026, 10, 1)
    assert prioritise([], today) == []