def can_register_thesis(credits: int, gpa: float) -> bool:
    if credits >= 120 and gpa >= 2.0:
        return True
    return False
    
def missing(credits, gpa) -> list[str]:
    if can_register_thesis(credits, gpa):
        return []
    reason = []
    if credits < 120:
        reason.append(f"need {120 - credits} more credits")
    if gpa < 2.0:
        reason.append(f"need {2.0 - gpa} more gpa")
    return reason
    