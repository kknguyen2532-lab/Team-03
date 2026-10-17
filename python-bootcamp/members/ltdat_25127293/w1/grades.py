def summary(scores: list[float]) -> dict:
    if not scores:
        raise ValueError("Danh sách rỗng")

    sorted_score = sorted(scores)
    n = len(sorted_score)

    min_val = sorted_score[0]
    max_val = sorted_score[-1]
    mean_val = round(sum(sorted_score) / n, 2)

    if n % 2 == 1:
        median_val = sorted_score[n // 2]
    else:
        median_val = round((sorted_score[n // 2 - 1] + sorted_score[n // 2]) / 2, 2)

    return {"min": min_val, "max": max_val, "mean": mean_val, "median": median_val}
