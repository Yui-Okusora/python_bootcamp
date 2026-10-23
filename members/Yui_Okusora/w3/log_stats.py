import math
from collections import Counter, defaultdict


def analyse(pairs: list[tuple[str, float | int]]) -> dict:
    """Thống kê lượt request, p95 latency của từng route và tìm route chậm nhất."""
    if not pairs:
        return {"counts" : Counter(), "p95" : {}, "slowest" : None}

    counts: Counter[str] = Counter()
    latencies: defaultdict[str, list[float]] = defaultdict(list)

    for route, latency in pairs:
        counts[route] += 1
        latencies[route].append(float(latency))

    p95_results: dict[str, float] = {}

    for route, times in latencies.items():
        times.sort()

        idx = math.ceil(0.95 * len(times)) - 1
        p95_results[route] = times[max(0,idx)]

    slowest_route = max(p95_results, key=lambda r: p95_results[r])

    return {"counts" : counts, "p95" : p95_results, "slowest" : slowest_route}
