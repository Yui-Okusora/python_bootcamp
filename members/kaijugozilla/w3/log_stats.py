from collections import Counter, defaultdict
from math import ceil


def analyse(pairs: list[tuple[str, float]]) -> dict:
    """Count requests and calculate p95 latency per route."""
    counts = Counter()
    latencies = defaultdict(list)

    for route, latency_ms in pairs:
        counts[route] += 1
        latencies[route].append(latency_ms)

    p95 = {}

    for route, values in latencies.items():
        sorted_values = sorted(values)
        rank = ceil(0.95 * len(sorted_values)) - 1
        p95[route] = sorted_values[rank]

    if p95:
        slowest = min(
            p95,
            key=lambda route: (-p95[route], route),
        )
    else:
        slowest = None

    return {
        "counts": dict(counts),
        "p95": p95,
        "slowest": slowest,
    }
