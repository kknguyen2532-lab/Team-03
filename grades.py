import statistics

def summary(scores: list[float]) -> dict:
    if not scores:
        raise ValueError("Danh sách điểm trống")
    return {
        "min": round(min(scores), 2),
        "max": round(max(scores), 2),
        "mean": round(statistics.mean(scores), 2),
        "median": round(statistics.median(scores), 2)
    }