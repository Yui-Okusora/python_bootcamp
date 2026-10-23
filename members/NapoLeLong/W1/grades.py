import statistics


def summary(scores: list[float]) -> dict:
    """Tính các thông số thống kê cơ bản (min, max, mean, median) từ danh sách điểm số."""
    if not scores:
        raise ValueError("the scores list is empty")
    else:
        min_val= min(scores)
        max_val=max(scores)
        mean_val=round(sum(scores)/len(scores),2)
        median_val=statistics.median(scores)
        return {
        "min": min_val,
        "max": max_val,
        "mean": mean_val,
        "median": median_val
        }