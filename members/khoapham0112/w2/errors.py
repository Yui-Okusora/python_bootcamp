"""Write a error to check if available hours is enough for the workload"""

class InfeasiblePlan(Exception):
    def __init__(self, needed_h: float, available_h: float):
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__()
    def __str__(self) -> str:
        return f"Plan is infeasible: needed {self.needed_h}h, but only {self.available_h}h available."

def check_feasible(tasks, available_h: float) -> bool:
    total_needed = sum(task.effort_h for task in tasks)
    if total_needed > available_h:
        raise InfeasiblePlan(needed_h=total_needed, available_h=available_h)
    return True