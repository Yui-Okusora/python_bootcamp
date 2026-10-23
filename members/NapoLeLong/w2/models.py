from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    """Mô tả thông tin đối tượng công việc."""
    title: str
    importance: int
    effort_h: float
    deadline: date
    def __post_init__(self) -> None:
        """Kiểm tra độ quan trọng của công việc (phải nằm trong khoảng từ 1 đến 5)."""
        if not 1 <= self.importance <= 5:
            raise ValueError("importance must be 1-5")
    def days_left(self, today: date) -> int:
        """Tính số ngày còn lại đến hạn chót (deadline) so với ngày hiện tại."""
        delta = (self.deadline - today).days
        return max(0, delta)