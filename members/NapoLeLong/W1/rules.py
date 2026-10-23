def can_register_thesis(credits: int, gpa: float) -> bool:
    """Kiểm tra điều kiện đăng ký khóa luận tốt nghiệp (yêu cầu ít nhất 120 tín chỉ và GPA >= 2.0)."""
    return credits >= 120 and gpa >= 2.0
def missing(credits: int,gpa: float) -> list[str]:
    """Trả về danh sách các tiêu chí còn thiếu để đủ điều kiện đăng ký khóa luận."""
    reason = []
    if credits<120:
        diff = 120 - credits
        reason.append(f"need {diff} more credit{'s' if diff != 1 else ''}")
    if gpa<2.0:
        diff = 2.0 - gpa
        reason.append(f"need {diff} more GPA")
    return reason