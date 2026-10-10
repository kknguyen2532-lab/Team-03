
def summary(scores: list[float]) -> dict:
    if len(scores) == 0:
        raise ValueError("scores must not be empty")

    min_score = min(scores)
    max_score = max(scores)

    mean_score = round(sum(scores) / len(scores), 2)

    sorted_scores = sorted(scores)
    n = len(sorted_scores)

    if n % 2 == 1:
        median_score = sorted_scores[n // 2]
    else:
        middle1 = sorted_scores[n // 2 - 1]
        middle2 = sorted_scores[n // 2]
        median_score = (middle1 + middle2) / 2

    median_score = round(median_score, 2)

    return {
        "min": min_score,
        "max": max_score,
        "mean": mean_score,
        "median": median_score
    }
