import csv
import json
from dataclasses import asdict
from datetime import date
from .models import Task

def load_tasks(path: str) -> list[Task]:
    tasks = []

    with open(path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for line_number, row in enumerate(reader, start=2):
            try:
                title = row["title"]
                importance = int(row["importance"])
                effort_h = float(row["effort_h"])
                deadline = date.fromisoformat(row["deadline"])

                task = Task(
                    title=title,
                    importance=importance,
                    effort_h=effort_h,
                    deadline=deadline,
                )
                tasks.append(task)

            except Exception as e:
                raise ValueError(
                    f"Invalid row at line {line_number}: {e}"
                ) from e

    return tasks


def save_json(tasks: list[Task], path: str) -> None:
    task_list = []
    for task in tasks:
        task_dict = asdict(task)
        task_dict["deadline"] = task.deadline.isoformat()
        task_list.append(task_dict)

    with open(path, mode="w", encoding="utf-8") as file:
        json.dump(task_list, file, indent=2, ensure_ascii=False)