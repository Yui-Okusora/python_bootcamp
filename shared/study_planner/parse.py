import csv
from datetime import date
from shared.contract import Task


def parse_csv(path: str) -> list[Task]:
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