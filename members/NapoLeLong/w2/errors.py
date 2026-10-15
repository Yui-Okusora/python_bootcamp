from typing import Iterable
from .models import Task

class InfeasiblePlan(Exception):
    def __init__(self, needed_h: float, available_h: float):
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(f"Kế hoạch khả bất thi: Cần {needed_h}h nhưng chỉ có {available_h}h.")
    def __str__(self):
        return self.args[0]
def check_feasible(tasks: Iterable[Task], available_h: float):
    needed_h = sum(task.effort_h for task in tasks)
    if needed_h > available_h:
        raise InfeasiblePlan(needed_h, available_h)