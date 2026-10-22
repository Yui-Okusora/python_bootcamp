"""Module định nghĩa các ngoại lệ tùy chỉnh và hàm kiểm tra tính khả thi của kế hoạch."""

from .models import Task


class InfeasiblePlan(Exception):
    """Ngoại lệ được ném ra khi tổng thời gian thực hiện vượt quá thời gian cho phép."""

    def __init__(self, needed_h: float, available_h: float) -> None:
        """Khởi tạo ngoại lệ InfeasiblePlan.

        Args:
            needed_h (float): Tổng số giờ cần thiết.
            available_h (float): Số giờ hiện có.
        """
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(
            f"Infeasible plan: needed {needed_h}h, but only {available_h}h available"
        )


def check_feasible(tasks: list[Task], available_h: float) -> None:
    """Kiểm tra tổng thời gian của danh sách công việc có vượt quá quỹ thời gian không.

    Args:
        tasks (list[Task]): Danh sách các công việc.
        available_h (float): Tổng thời gian khả dụng (giờ).

    Raises:
        InfeasiblePlan: Nếu tổng thời gian thực hiện lớn hơn thời gian khả dụng.
    """
    total_needed = sum(task.effort_h for task in tasks)
    if total_needed > available_h:
        raise InfeasiblePlan(needed_h=total_needed, available_h=available_h)