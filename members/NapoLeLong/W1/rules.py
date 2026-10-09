def can_register_thesis(credits: int, gpa: float) -> bool:
    return credits >= 120 and gpa >= 2.0
def missing(credits: int,gpa: float) -> list[str]:
    reason = []
    if can_register_thesis(credits, gpa) == True:
        reason.append("no missing requirements")
    else:
        if credits<120:
            diff = 120 - credits
            reason.append(f"need {diff} more credit{'s' if diff != 1 else ''}")
        if gpa<2.0:
            diff = 2.0 - gpa
            reason.append(f"need {diff} more GPA")
    return reason