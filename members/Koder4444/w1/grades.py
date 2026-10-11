def summary(scores: list[float]) -> dict:
    if not scores:
        raise ValueError("scores must not be empty")
    
    min_val = min(scores)
    max_val = max(scores)
    
    n = len(scores)
    mean = sum(scores) / n
    
    sorted_scores = sorted(scores)
    
    if n % 2 != 0:
        median = sorted_scores[n // 2]
    else:
        mid1 = (n // 2) - 1
        mid2 = n // 2
        median = (sorted_scores[mid1] + sorted_scores[mid2]) / 2
    
    return {
        "min": min_val,
        "max": max_val,
        "mean": round(mean, 2),
        "median": round(median, 2)
    }