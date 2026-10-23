import math
from collections import Counter, defaultdict
from typing import Any


def analyse(pairs: list[tuple[str, float | int]]) -> dict[str, Any]:
    """Analyse latency log pairs and return request counts, p95 latency, and the slowest route."""
    if not pairs:
        return {"counts": Counter(), "p55": {}, "p95": {}, "slowest": None}

    counts = Counter()
    latencies = defaultdict(list)

    for route, latency in pairs:
        counts[route] += 1
        latencies[route].append(latency)

    p95_per_route = {}
    for route, lat_list in latencies.items():
        sorted_lats = sorted(lat_list)
        n = len(sorted_lats)
        
        idx = math.ceil(0.95 * n) - 1
        p95_per_route[route] = sorted_lats[idx]

    slowest_route = max(p95_per_route, key=p95_per_route.get) if p95_per_route else None

    return {
        "counts": counts,
        "p95": p95_per_route,
        "slowest": slowest_route
    }