import statistics


def summary(scores: list[float]) -> dict:
    if not scores:
        raise ValueError("the scores list is empty")
    else:
        min_val= min(scores)
        max_val=max(scores)
        mean_val=sum(scores)/len(scores)
        median_val=statistics.median(scores)
        return {
        "min": min_val,
        "max": max_val,
        "mean": mean_val,
        "median": median_val
        }