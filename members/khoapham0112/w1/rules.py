"""return bool if credits >= 120 and gpa >= 2"""
def can_register_thesis(credits: int, gpa: float) -> list[str]:
    return bool((credits >= 120) & (gpa >= 2))
"""return message if with that gpa and credits can register thesis or not"""
def missing(credits, gpa):
    if can_register_thesis(credits, gpa):
        return []
    else:
        reasons = []
        missing_credits = 120 - credits
        missing_gpa = 2 - gpa
        if(missing_credits > 0):
            reasons.append(f"need {missing_credits} more credits")
        if(missing_gpa > 0):
            reasons.append(f"need {missing_gpa} more gpa.")
    return reasons

print(missing(120, 3))