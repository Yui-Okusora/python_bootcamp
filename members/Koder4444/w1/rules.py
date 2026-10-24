def can_register_thesis(credits: int, gpa: float) -> bool:
    """Check if a student meets the minimum credit and GPA criteria to register for a thesis."""
    return credits >= 120 and gpa >= 2.0


def missing(credits: int, gpa: float) -> list[str]:
    """Return a list of unmet requirements for thesis registration."""
    if can_register_thesis(credits, gpa):
        return []
    
    reason: list[str] = []
    if credits < 120:
        reason.append(f"need {120 - credits} more credits")
    if gpa < 2.0:
        reason.append(f"need {2.0 - gpa:.2f} more gpa")
        
    return reason