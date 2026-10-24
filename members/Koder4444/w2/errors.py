from members.Koder4444.w2.models import Task


class InfeasiblePlan(Exception):
    """Exception raised when the total task effort exceeds available hours."""

    def __init__(self, needed_h: float, available_h: float) -> None:
        """Initialize the exception with needed and available hours."""
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(
            f"Infeasible plan: needed {needed_h}h, but only {available_h}h available."
        )

    def __str__(self) -> str:
        """Return a string representation of the exception."""
        return (
            f"Infeasible plan: needed {self.needed_h}h, available {self.available_h}h"
        )


def check_feasible(tasks: list[Task], available_h: float) -> None:
    """Check if the total effort of all tasks is within the available hours."""
    needed_h = sum(task.effort_h for task in tasks)
    if needed_h > available_h:
        raise InfeasiblePlan(needed_h, available_h)