import csv
import json
from datetime import date
from .models import Task

def load_tasks(path: str) -> list[Task]:
    tasks = []
    with open(path, mode='r') as f:
        reader = csv.reader(f)
        header = next(reader, None) 
        if not header:
            return tasks        
        for line_num, row in enumerate(reader, start=2):
            try:
                if len(row) < 4:
                    raise ValueError("Missing data column")
                title = row[0].strip()
                importance = int(row[1].strip())
                effort_h = float(row[2].strip())
                deadline = date.fromisoformat(row[3].strip())
                task = Task(
                    title=title, 
                    importance=importance, 
                    effort_h=effort_h, 
                    deadline=deadline
                )
                tasks.append(task)
            except Exception as e:
                raise ValueError(f"Error line {line_num}: {e}")                
    return tasks
def save_json(tasks: list[Task], path: str):
    data = []
    for t in tasks:
        data.append({
            "title": t.title,
            "importance": t.importance,
            "effort_h": t.effort_h,
            "deadline": t.deadline.isoformat()
        })
    with open(path, mode='w') as f:
        json.dump(data, f, indent=4)