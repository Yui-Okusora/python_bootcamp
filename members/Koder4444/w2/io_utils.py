import csv
import json
from dataclasses import asdict
from datetime import date

from members.Koder4444.w2.models import Task


def load_tasks(path: str) -> list[Task]:
    tasks = []
    with open(path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                task = Task(
                    title=row["title"].strip(),
                    importance=int(row["importance"]),
                    effort_h=float(row["effort_h"]),
                    deadline=date.fromisoformat(row["deadline"].strip()),
                )
                tasks.append(task)
            except (ValueError, KeyError, AttributeError) as e:
                raise ValueError(f"Invalid row at line {reader.line_num}: {e}")
    return tasks


def save_json(tasks: list[Task], path: str) -> None:
    data = []
    for task in tasks:
        task_dict = asdict(task)
        task_dict["deadline"] = task.deadline.isoformat()
        data.append(task_dict)

    with open(path, mode="w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)