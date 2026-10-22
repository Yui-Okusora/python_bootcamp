from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    """Store task information and its deadline."""
    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self) -> None:
        """Check that importance is between 1 and 5."""
        if not 1 <= self.importance <= 5:
            raise ValueError("importance must be 1-5")

    def days_left(self, today: date) -> int:
        """Return the days left until the deadline."""
        days = (self.deadline - today).days
        return max(days, 0)
