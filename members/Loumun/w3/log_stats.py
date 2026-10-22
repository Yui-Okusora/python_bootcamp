"""Module phân tích nhật ký (log) và thống kê chỉ số hiệu năng."""

import math
from collections import Counter, defaultdict
from typing import Any


def analyse(pairs: list[tuple[str, float]]) -> dict[str, Any]:
    """Phân tích danh sách log độ trễ để tính lượt truy cập và chỉ số percentile 95.

    Args:
        pairs (list[tuple[str, float]]): Danh sách các cặp (route_path, latency).

    Returns:
        dict[str, Any]: Tự điển chứa lượt gọi ('counts'), chỉ số 'p95', và route chậm nhất ('slowest').
    """
    counts: Counter[str] = Counter()
    latencies: dict[str, list[float]] = defaultdict(list)

    for route, lat in pairs:
        counts[route] += 1
        latencies[route].append(lat)

    p95: dict[str, float] = {}
    for route, lats in latencies.items():
        lats.sort()
        idx = max(0, math.ceil(0.95 * len(lats)) - 1)
        p95[route] = lats[idx]

    slowest = max(p95, key=lambda k: p95[k]) if p95 else None

    return {"counts": counts, "p95": p95, "slowest": slowest}