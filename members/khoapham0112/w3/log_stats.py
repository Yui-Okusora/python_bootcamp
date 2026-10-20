from collections import Counter, defaultdict
import math

def analyse(pairs) -> dict:
    if not pairs:
        return {"counts": Counter(), "p95": {}, "slowest": None}

    routes = defaultdict(list)
    counts = Counter()

    for route, latency in pairs:
        routes[route].append(latency)
        counts[route] += 1

    p95 = {}
    for route, latencies in routes.items():
        sorted_lat = sorted(latencies)
        n = len(sorted_lat)
        idx = max(0, math.ceil(0.95 * n) - 1)
        p95[route] = sorted_lat[idx]

    slowest = max(p95, key=p95.get)

    return {
        "counts": counts,
        "p95": p95,
        "slowest": slowest
    }