import os
import tempfile
from datetime import date

from shared.study_planner.parse import parse_csv


def test_parse_csv_valid() -> None:
    """Test parsing a valid CSV file using standard assertions."""
    with tempfile.NamedTemporaryFile(mode="w", delete=False, encoding="utf-8", suffix=".csv") as tmp:
        tmp.write(
            "title,importance,effort_h,deadline\n"
            "Math Exam,5,3.5,2026-11-10\n"
            "Physics Lab,3,2.0,2026-11-12\n"
        )
        tmp_path = tmp.name

    try:
        tasks = parse_csv(tmp_path)
        assert len(tasks) == 2, f"Expected 2 tasks, got {len(tasks)}"
        assert tasks[0].title == "Math Exam"
        assert tasks[0].importance == 5
        assert tasks[0].effort_h == 3.5
        assert tasks[0].deadline == date(2026, 11, 10)
        print("test_parse_csv_valid: SUCCESS")
    finally:
        os.remove(tmp_path)


def test_parse_csv_invalid_row() -> None:
    """Test that invalid row raises ValueError with line number using try-except."""
    with tempfile.NamedTemporaryFile(mode="w", delete=False, encoding="utf-8", suffix=".csv") as tmp:
        tmp.write(
            "title,importance,effort_h,deadline\n"
            "Bad Task,10,1.5,2026-11-10\n"
        )
        tmp_path = tmp.name

    try:
        parse_csv(tmp_path)
        raise AssertionError("Expected ValueError but no exception was raised.")
    except ValueError as e:
        assert "line 2" in str(e), f"Expected message to contain 'line 2', got: {e}"
        print("test_parse_csv_invalid_row: SUCCESS")
    finally:
        os.remove(tmp_path)


if __name__ == "__main__":
    print("Running manual tests...")
    test_parse_csv_valid()
    test_parse_csv_invalid_row()
    print("All tests passed successfully!")