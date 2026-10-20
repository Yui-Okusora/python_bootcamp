import csv
import datetime
import json
from dataclasses import asdict, dataclass


@dataclass
class Task:
    title: str
    importance: int
    effort_h: float
    deadline: datetime.date
   
    def __post_init__(self):
        if not 1 <= self.importance <= 5:
            raise ValueError("importance must be 1-5")

"""load task from the csv file"""
def load_tasks(path: str) -> list[Task]:
    tasks = []
    with open(path, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader, None)
        print(header)
        for line_num, row in enumerate(reader, start=2):
            title_val = row[0].strip()
            try:
                importance_val = int(row[1].strip())
                effort_val = float(row[2].strip())
                deadline_val = datetime.date.fromisoformat(row[3].strip())
                task = Task(title_val, importance_val, effort_val, deadline_val)
                tasks.append(task)
            except (FileNotFoundError, ValueError, OSError) as e:
                raise ValueError(f"Invalid data at line {line_num}: {e}")
                
    return tasks
"""Save task into a json format"""
def save_json(tasks: list[Task], path: str):
    data = []
    for task in tasks:
        task_dict = asdict(task)
        task_dict['deadline'] = task.deadline.isoformat()
        data.append(task_dict)
        
    with open(path, mode='w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)