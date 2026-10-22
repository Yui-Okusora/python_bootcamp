def can_register_thesis(credits: int, gpa: float) -> bool:
    """Check if a student is eligible to register for a thesis."""
    return credits >= 120 and gpa >= 2.0

def missing(credits: int, gpa: float) -> list[str]:
    """Return the requirements a student has not met."""
    reasons = []

    if credits < 120:
        needed = 120 - credits
        reasons.append(f"need {needed} more credits")

    if gpa < 2.0:
        reasons.append("GPA must be at least 2.0")

    return reasons
