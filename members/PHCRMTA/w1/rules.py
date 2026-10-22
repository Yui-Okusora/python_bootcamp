def can_register_thesis(credits: int, gpa: float) -> bool:
    """Check if a student meets the requirements to register for a thesis."""
    return credits >= 120 and gpa >= 2.0


def missing(credits: int, gpa: float) -> list[str]:
    """Return a list of reasons why a student cannot register for a thesis."""
    reasons = []

    if credits < 120:
        needed_credits = 120 - credits
        reasons.append(f"need {needed_credits} more credits")

    if gpa < 2.0:
        reasons.append("GPA must be at least 2.0")

    return reasons