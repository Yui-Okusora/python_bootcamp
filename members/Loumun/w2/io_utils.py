"""Module hỗ trợ đọc và ghi dữ liệu công việc ra file (CSV, JSON)."""

import csv
import json
from dataclasses import asdict
from datetime import date
from pathlib import Path
from typing import Any

from .models import Task


def load_tasks(path: str | Path) -> list[Task]:
    """Tải danh sách các công việc từ file CSV.

    Args:
        path (str | Path): Đường dẫn đến file CSV cần đọc.

    Returns:
        list[Task]: Danh sách đối tượng Task được khởi tạo từ file CSV.

    Raises:
        ValueError: Nếu cấu trúc dòng hoặc dữ liệu trong file CSV không hợp lệ.
    """
    tasks: list[Task] = []
    with open(path, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader, None)

        for line_num, row in enumerate(reader, start=2):
            if not row:
                continue

            if len(row) != 4:
                raise ValueError(
                    f"Line {line_num}: Expected 4 columns, got {len(row)}"
                )

            title, importance_str, effort_str, deadline_str = [
                col.strip() for col in row
            ]

            try:
                importance = int(importance_str)
                effort_h = float(effort_str)
                deadline = date.fromisoformat(deadline_str)

                task = Task(
                    title=title,
                    importance=importance,
                    effort_h=effort_h,
                    deadline=deadline,
                )
                tasks.append(task)
            except ValueError as exc:
                raise ValueError(
                    f"Line {line_num}: Invalid row format ({exc})"
                ) from exc
    return tasks


def save_json(tasks: list[Task], path: str | Path) -> None:
    """Lưu danh sách công việc xuống file định dạng JSON.

    Args:
        tasks (list[Task]): Danh sách các đối tượng Task.
        path (str | Path): Đường dẫn file JSON đầu ra.
    """

    def date_serializer(obj: Any) -> str:
        if isinstance(obj, date):
            return obj.isoformat()
        raise TypeError(f"Type {type(obj)} is not JSON serializable")

    tasks_data = [asdict(task) for task in tasks]

    with open(path, mode="w", encoding="utf-8") as file:
        json.dump(
            tasks_data,
            file,
            default=date_serializer,
            indent=4,
            ensure_ascii=False,
        )