import csv
from datetime import date

from shared.contract import Task


def parse_csv(path: str) -> list[Task]:
    """Read a CSV file with header and return a list of Task objects.
    
    Raises ValueError with line number if any row is invalid.
    """
    tasks = []
    with open(path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                importance_val = int(row["importance"])
                if not (1 <= importance_val <= 5):
                    raise ValueError("importance must be between 1 and 5")

                task = Task(
                    title=row["title"].strip(),
                    importance=importance_val,
                    effort_h=float(row["effort_h"]),
                    deadline=date.fromisoformat(row["deadline"].strip()),
                )
                tasks.append(task)
            except (ValueError, KeyError, TypeError) as e:
                raise ValueError(f"Invalid row at line {reader.line_num}: {e}")
                
    return tasks