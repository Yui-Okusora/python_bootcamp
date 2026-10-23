from collections.abc import Iterable

from .models import Task


class InfeasiblePlan(Exception):
    """Ngoại lệ được ném ra khi tổng thời gian công việc vượt quá thời gian cho phép."""
    def __init__(self, needed_h: float, available_h: float) -> None:
        """Khởi tạo ngoại lệ với số giờ cần thiết và số giờ khả dụng."""
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(f"Infeasible plan: needed {needed_h}h but only {available_h}h available.")
    def __str__(self) -> str:
        """Trả về thông báo lỗi chi tiết."""
        return self.args[0]
def check_feasible(tasks: Iterable[Task], available_h: float) -> None:
    """Kiểm tra tổng thời gian thực hiện công việc có vượt quá giới hạn thời gian hay không."""
    needed_h = sum(task.effort_h for task in tasks)
    if needed_h > available_h:
        raise InfeasiblePlan(needed_h, available_h)