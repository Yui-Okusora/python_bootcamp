import statistics


def summary(scores: list[float]) -> dict:
    min_val, max_val = min(scores), max(scores)
    mean_val=sum(scores)/len(scores)
    median_val=statistics.median(scores)
    return {
        "min": min_val,
        "max": max_val,
        "mean": mean_val,
        "median": median_val
    }
