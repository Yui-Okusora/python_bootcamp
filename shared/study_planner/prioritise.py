import os
import sys

thu_muc_cha = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.insert(0, thu_muc_cha)
import datetime

from contract import Task


def days_left(task, today: datetime.date):
       diff = task.deadline - today
       if(diff.days <= 0):
           return 100000
       return diff.days

def prioritise(tasks, today) -> list[Task]:
    res = {}
    for task in tasks:
         diff = days_left(task, today)
         prioritise_val = task.importance / diff
         res.setdefault(prioritise_val, [])
         res[prioritise_val].append(task)
    sorted_res = dict(sorted(res.items(), reverse= True))
    return [value for values in sorted_res.values() for value in values]
