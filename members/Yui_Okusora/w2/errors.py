from .models import Task


class InfeasiblePlan(Exception):

  def __init__(self, needed_h: float, available_h: float):
    self.needed_h = needed_h
    self.available_h = available_h

  def __str__(self) -> str:
    return (
        f'Plan infeasible: Need {self.needed_h}h while'
        f' {self.available_h}h available.'
    )


def check_feasible(tasks: list[Task], available_h: float) -> None:
  """Check required time not exceed limit"""
  needed_h = sum(task.effort_h for task in tasks)
  if needed_h > available_h:
    raise InfeasiblePlan(needed_h=needed_h, available_h=available_h)