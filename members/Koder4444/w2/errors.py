from members.Koder4444.w2.models import Task


class InfeasiblePlan(Exception):
    def __init__(self, needed_h: float, available_h: float) -> None:
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(
            f"Infeasible plan: needed {needed_h}h, but only {available_h}h available."
        )

    def __str__(self) -> str:
        return (
            f"Infeasible plan: needed {self.needed_h}h, available {self.available_h}h"
        )


def check_feasible(tasks: list[Task], available_h: float) -> None:
    needed_h = sum(task.effort_h for task in tasks)
    if needed_h > available_h:
        raise InfeasiblePlan(needed_h, available_h)
