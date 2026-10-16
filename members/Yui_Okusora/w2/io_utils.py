import csv
import json
from datetime import date
from pathlib import Path

from .models import Task


def load_tasks(path: str | Path) -> list[Task]:
  """Read csv file and return task list"""
  tasks = []
  path = Path(path)

  with open(path, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)

    for line_num, row in enumerate(reader, start=2):
      try:
        title = row['title'].strip()
        importance = int(row['importance'])
        effort_h = float(row['effort_h'])
        deadline = date.fromisoformat(row['deadline'].strip())

        task = Task(
            title=title,
            importance=importance,
            effort_h=effort_h,
            deadline=deadline,
        )
        tasks.append(task)
      except (KeyError, ValueError) as err:
        raise ValueError(
            f'Record invalid at line {line_num}: {err}'
        ) from err

  return tasks


def save_json(tasks: list[Task], path: str | Path) -> None:
  """Save task list into JSON file"""
  path = Path(path)
  data = [
      {
          'title': t.title,
          'importance': t.importance,
          'effort_h': t.effort_h,
          'deadline': t.deadline.isoformat(),
      }
      for t in tasks
  ]

  with open(path, mode='w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)