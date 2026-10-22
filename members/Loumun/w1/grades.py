"""Module cung cấp các hàm tính toán thống kê bảng điểm."""


def summary(scores: list[float]) -> dict[str, float]:
    """Tính toán các thông số thống kê cơ bản từ danh sách điểm số.

    Args:
        scores (list[float]): Danh sách điểm số cần thống kê.

    Returns:
        dict[str, float]: Tự điển chứa các giá trị 'min', 'max', 'mean', và 'median'.

    Raises:
        ValueError: Nếu danh sách điểm đầu vào bị rỗng.
    """
    if not scores:
        raise ValueError("the scores list is empty")

    min_val = float(scores[0])
    max_val = float(scores[0])
    total_score = 0.0

    for score in scores:
        min_val = min(score, min_val)
        max_val = max(score, max_val)
        total_score += score

    mean_val = total_score / len(scores)

    sorted_scores = sorted(scores)
    n = len(sorted_scores)
    if n % 2 == 0:
        median_val = (sorted_scores[n // 2 - 1] + sorted_scores[n // 2]) / 2
    else:
        median_val = float(sorted_scores[n // 2])

    return {
        "min": min_val,
        "max": max_val,
        "mean": round(mean_val, 2),
        "median": round(median_val, 2),
    }