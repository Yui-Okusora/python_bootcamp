from collections import Counter, defaultdict
import math


def calculate_p95(latencies: list[float]) -> float:
    """Calculate the 95th percentile latency from a list of latency values."""
    if not latencies:
        return 0.0
    sorted_latencies = sorted(latencies)
    n = len(sorted_latencies)
    index = math.ceil(0.95 * n) - 1
    return float(sorted_latencies[index])


def analyse(pairs: list[tuple[str, float]]) -> dict:
    """Analyze route latencies to return counts, 95th percentiles, and the slowest route."""
    if not pairs:
        return {"counts": Counter(), "p95": {}, "slowest": None}

    route_latencies = defaultdict(list)
    counts = Counter()

    for route, latency in pairs:
        route_latencies[route].append(latency)
        counts[route] += 1

    p95_dict = {}
    for route, latencies in route_latencies.items():
        p95_dict[route] = calculate_p95(latencies)

    slowest_route = max(p95_dict, key=p95_dict.get) if p95_dict else None

    return {
        "counts": counts,
        "p95": p95_dict,
        "slowest": slowest_route,
    }