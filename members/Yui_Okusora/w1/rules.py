def can_register_thesis(credits: int, gpa: float) -> bool:
    """Check thesis registration eligibility."""
    return credits >= 120 and gpa >= 2.0


def missing(credits: int, gpa: float) -> list[str]:
    """Return list of eligibility failure reasons."""
    reasons: list[str] = []

    if credits < 120:
        needed = 120 - credits
        if needed == 1:
            reasons.append("need 1 more credit")
        else:
            reasons.append(f"need {needed} more credits")

    if gpa < 2.0:
        reasons.append(f"GPA must be at least 2.0 (current GPA: {gpa})")

    return reasons