"""Chat log latency analysis utilities for Week 3 homework (W3-2)."""

import math
from collections import Counter, defaultdict
from collections.abc import Iterable
from typing import Any


def _percentile_95(values: list[float]) -> float:
    """Return the 95th percentile of a non-empty list using nearest-rank."""
    sorted_vals = sorted(values)
    index = max(0, math.ceil(0.95 * len(sorted_vals)) - 1)
    return sorted_vals[index]


def analyse(pairs: Iterable[tuple[str, float]]) -> dict[str, Any]:
    """Analyse (route, latency_ms) pairs and compute counts, p95, and slowest route."""
    counts: Counter[str] = Counter()
    latencies_by_route: defaultdict[str, list[float]] = defaultdict(list)

    for route, latency_ms in pairs:
        if latency_ms < 0:
            raise ValueError("latency_ms must be non-negative")
        counts[route] += 1
        latencies_by_route[route].append(float(latency_ms))

    if not counts:
        raise ValueError("pairs cannot be empty")

    p95: dict[str, float] = {
        route: _percentile_95(lats) for route, lats in latencies_by_route.items()
    }
    slowest: str = max(p95, key=lambda r: p95[r])

    return {
        "counts": counts,
        "p95": p95,
        "slowest": slowest,
    }
