"""Chat log analysis utility computing request counts and p95 latencies."""

from collections import Counter, defaultdict
import math
from typing import Any


def _compute_p95(latencies: list[float]) -> float:
    """Compute the 95th percentile latency using nearest-rank."""
    if not latencies:
        return 0.0
    sorted_latencies = sorted(latencies)
    index = math.ceil(0.95 * len(sorted_latencies)) - 1
    return float(sorted_latencies[index])


def analyse(pairs: list[tuple[str, float]]) -> dict[str, Any]:
    """Analyze route latencies and request counts.

    Returns:
        dict with keys:
          - "counts": Counter of calls per route
          - "p95": dict mapping route to its p95 latency
          - "slowest": the route name with the highest p95 latency
    """
    if not pairs:
        return {"counts": Counter(), "p95": {}, "slowest": None}

    counts: Counter[str] = Counter()
    route_latencies: dict[str, list[float]] = defaultdict(list)

    for route, latency in pairs:
        counts[route] += 1
        route_latencies[route].append(latency)
    p95_stats = {route: _compute_p95(lats) for route, lats in route_latencies.items()}
    slowest_route = max(p95_stats.items(), key=lambda item: item[1])[0]
    return {
        "counts": counts,
        "p95": p95_stats,
        "slowest": slowest_route,
    }
