import csv
import json
from dataclasses import asdict
from datetime import date
from .models import Task


def load_tasks(path: str) -> list[Task]:
    tasks = []
    with open(path, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        header = next(reader, None)

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
            except Exception as exc:
                raise ValueError(
                    f"Line {line_num}: Invalid row format ({exc})"
                ) from exc
    return tasks


def save_json(tasks: list[Task], path: str) -> None:
    def date_serializer(obj):
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