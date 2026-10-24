from collections import Counter, defaultdict
from collections.abc import Iterable
from math import ceil


def analyse(
    pairs: Iterable[tuple[str, float]],
) -> dict[str, object]:
    """Summarise request counts and p95 latency by route."""
    counts: Counter[str] = Counter()
    latencies: dict[str, list[float]] = defaultdict(list)

    for route, latency_ms in pairs:
        counts[route] += 1
        latencies[route].append(float(latency_ms))

    p95: dict[str, float] = {}

    for route, values in latencies.items():
        ordered = sorted(values)
        rank = max(1, ceil(0.95 * len(ordered)))
        p95[route] = ordered[rank - 1]

    slowest = max(p95, key=p95.get) if p95 else None

    return {
        "counts": counts,
        "p95": p95,
        "slowest": slowest,
    }