"""Module kiểm tra điều kiện đăng ký khóa luận tốt nghiệp của sinh viên."""


def can_register_thesis(credits: int, gpa: float) -> bool:
    """Kiểm tra sinh viên có đủ điều kiện đăng ký khóa luận hay không.

    Args:
        credits (int): Số tín chỉ hiện có.
        gpa (float): Điểm trung bình tích lũy (GPA).

    Returns:
        bool: True nếu đủ điều kiện (>= 120 tín chỉ và GPA >= 2.0), ngược lại False.
    """
    return credits >= 120 and gpa >= 2.0


def missing(credits: int, gpa: float) -> list[str]:
    """Liệt kê các điều kiện chưa đạt để đăng ký khóa luận.

    Args:
        credits (int): Số tín chỉ hiện có.
        gpa (float): Điểm trung bình tích lũy (GPA).

    Returns:
        list[str]: Danh sách các lý do chưa đủ điều kiện.
    """
    if can_register_thesis(credits, gpa):
        return []

    reasons: list[str] = []
    missing_credits = 120 - credits
    missing_gpa = 2.0 - gpa

    if missing_credits > 0:
        reasons.append(f"need {missing_credits} more credits")
    if missing_gpa > 0:
        reasons.append(f"need {round(missing_gpa, 2)} more gpa.")

    return reasons


if __name__ == "__main__":
    print(missing(120, 3.0))