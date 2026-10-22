"""Module chứa mô hình dữ liệu (Data models) cho ứng dụng."""

from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    """Mô tả thông tin chi tiết của một công việc.

    Attributes:
        title (str): Tên công việc.
        importance (int): Mức độ quan trọng (từ 1 đến 5).
        effort_h (float): Ước tính số giờ cần thực hiện.
        deadline (date): Hạn chót hoàn thành.
    """

    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self) -> None:
        """Kiểm tra tính hợp lệ của thuộc tính quan trọng sau khi khởi tạo.

        Raises:
            ValueError: Nếu mức độ quan trọng nằm ngoài khoảng 1 đến 5.
        """
        if not 1 <= self.importance <= 5:
            raise ValueError("importance must be 1-5")

    def days_left(self, today: date) -> int:
        """Tính số ngày còn lại đến hạn chót công việc.

        Args:
            today (date): Ngày hiện tại để so sánh.

        Returns:
            int: Số ngày còn lại (Trả về 0 nếu đã quá hạn).
        """
        remaining = (self.deadline - today).days
        return max(0, remaining)