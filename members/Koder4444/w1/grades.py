def summary(scores: list[float]) -> dict:
    if not scores:
        raise ValueError("scores must not be empty")
    
    min_val = min(scores)
    max_val = max(scores)
    
    n = len(scores)
    mean = sum(scores) / n
    
    if n % 2 == 0:
        median = (scores[n//2 - 1] + scores[n//2]) / 2
    else:
        median = scores[n//2]
    
    return {
        "min": min_val,
        "max": max_val,
        "mean": round(mean, 2),
        "meadian": round(median, 2)
    }