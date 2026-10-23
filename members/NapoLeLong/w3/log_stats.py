import math
from collections import Counter, defaultdict
from typing import Any


def analyse(pairs: list[tuple[str, float]]) -> dict[str, Any]:
    """Thống kê số lượng truy cập, tính p95 độ trễ và tìm route chậm nhất từ dữ liệu log."""
    counts = Counter()
    latencies = defaultdict(list)
    
    for route, latency in pairs:
        counts[route] += 1
        latencies[route].append(latency)
        
    p95_dict = {}
    for route, lats in latencies.items():
        lats.sort()
        idx = math.ceil(0.95 * len(lats)) - 1
        idx = max(0, min(idx, len(lats) - 1))
        p95_dict[route] = lats[idx]
        
    slowest_route = max(p95_dict, key=p95_dict.get) if p95_dict else None
    
    return {
        "counts": counts,
        "p95": p95_dict,
        "slowest": slowest_route
    }