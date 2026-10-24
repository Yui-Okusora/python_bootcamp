from datetime import date
from unittest.mock import patch

import pytest
from members.Koder4444.w2.errors import InfeasiblePlan
from shared.contract import Block, Task
from shared.study_planner.__main__ import main


def test_main_success(monkeypatch):
    dummy_task = Task("Assignment", 5, 1.5, date(2026, 12, 31))
    dummy_block = Block(dummy_task, 1.5)

    with (
        patch(
            "shared.study_planner.__main__.parse_csv",
            return_value=[dummy_task],
        ),
        patch(
            "shared.study_planner.__main__.prioritise",
            return_value=[dummy_task],
        ),
        patch("shared.study_planner.__main__.check_feasible"),
        patch(
            "shared.study_planner.__main__.allocate",
            return_value=[dummy_block],
        ),
        patch("shared.study_planner.__main__.render", return_value="Output"),
    ):
        monkeypatch.setattr(
            "sys.argv", ["_main_.py", "dummy.csv", "--hours", "2.0"]
        )
        main()  # Không bắn ra SystemExit là đạt


def test_main_empty_tasks_raises_exit(monkeypatch):
    with patch("shared.study_planner.__main__.parse_csv", return_value=[]):
        monkeypatch.setattr(
            "sys.argv", ["_main_.py", "empty.csv", "--hours", "2.0"]
        )

        with pytest.raises(SystemExit) as exc_info:
            main()

        assert exc_info.value.code == 1


def test_main_file_not_found_raises_exit(monkeypatch):
    with patch(
        "shared.study_planner.__main__.parse_csv",
        side_effect=FileNotFoundError,
    ):
        monkeypatch.setattr(
            "sys.argv", ["_main_.py", "missing.csv", "--hours", "2.0"]
        )

        with pytest.raises(SystemExit) as exc_info:
            main()

        assert exc_info.value.code == 1


def test_main_infeasible_plan_raises_exit(monkeypatch):
    dummy_task = Task("Heavy Task", 5, 10.0, date(2026, 12, 31))

    with (
        patch(
            "shared.study_planner.__main__.parse_csv",
            return_value=[dummy_task],
        ),
        patch(
            "shared.study_planner.__main__.check_feasible",
            side_effect=InfeasiblePlan(10.0, 2.0),
        ),
    ):
        monkeypatch.setattr(
            "sys.argv", ["_main_.py", "dummy.csv", "--hours", "2.0"]
        )

        with pytest.raises(SystemExit) as exc_info:
            main()

        assert exc_info.value.code == 1


def test_main_value_error_raises_exit(monkeypatch):
    with patch(
        "shared.study_planner.__main__.parse_csv", side_effect=ValueError
    ):
        monkeypatch.setattr(
            "sys.argv", ["_main_.py", "invalid.csv", "--hours", "2.0"]
        )

        with pytest.raises(SystemExit) as exc_info:
            main()

        assert exc_info.value.code == 1
