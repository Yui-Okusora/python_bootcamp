from .models import Task


class InfeasiblePlan(Exception):
    """Report when tasks need more hours than available."""

    def __init__(self, needed_h: float, available_h: float) -> None:
        """Store the required and available hours."""
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(str(self))

    def __str__(self) -> str:
        """Return a readable error message."""
        return (
            f"Plan needs {self.needed_h} hours, "
            f"but only {self.available_h} hours are available."
        )


def check_feasible(tasks: list[Task], available_h: float) -> None:
    """Raise InfeasiblePlan when total task hours exceed available hours."""
    needed_h = sum(task.effort_h for task in tasks)
    if needed_h > available_h:
        raise InfeasiblePlan(needed_h, available_h)
