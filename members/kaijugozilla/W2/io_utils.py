import csv
import json
from datetime import date
from pathlib import Path

from .models import Task

def load_tasks(path: str | Path) -> list[Task]:
    tasks = []

    with open(path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        expected = ["title", "importance", "effort_h", "deadline"]

        if reader.fieldnames != expected:
            raise ValueError("Invalid CSV header at line 1")

        for row in reader:
            line_number = reader.line_num

            try:
                if None in row or any(
                    row[name] is None for name in expected
                ):
                    raise ValueError("incorrect number of columns")

                task = Task(
                    title=row["title"].strip(),
                    importance=int(row["importance"]),
                    effort_h=float(row["effort_h"]),
                    deadline=date.fromisoformat(
                        row["deadline"].strip()
                    ),
                )

                if not task.title:
                    raise ValueError("title cannot be empty")

                tasks.append(task)

            except (ValueError, TypeError) as error:
                raise ValueError(
                    f"Invalid row at line {line_number}: {error}"
                ) from error

    return tasks


def save_json(tasks: list[Task], path: str | Path) -> None:
    data = []

    for task in tasks:
        data.append({
            "title": task.title,
            "importance": task.importance,
            "effort_h": task.effort_h,
            "deadline": task.deadline.isoformat(),
        })

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
