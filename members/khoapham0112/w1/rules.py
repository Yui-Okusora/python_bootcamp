def can_register_thesis(credits: int, gpa: float):
    if (credits >= 120) & (gpa >= 2):
        return True
    else:
        return False
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