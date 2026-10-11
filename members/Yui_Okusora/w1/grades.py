def summary(scores: list[float]) -> dict[str, float]:
    """Calculate min, max, mean, and median using manual loop iteration."""
    if not scores:
        raise ValueError("Scores list cannot be empty.")

    n = len(scores)
    min_val = scores[0]
    max_val = scores[0]
    total_sum = 0.0

    for i in range(n):
        val = scores[i]
        min_val = min(min_val, val)
        max_val = max(max_val, val)
        total_sum += val

    mean_val = total_sum / n

    sorted_scores = sorted(scores)
    if n % 2 == 1:
        median_val = sorted_scores[n // 2]
    else:
        median_val = (sorted_scores[(n // 2) - 1] + sorted_scores[n // 2]) / 2.0

    return {
        "min": min_val,
        "max": max_val,
        "mean": round(mean_val, 2),
        "median": round(median_val, 2),
    }