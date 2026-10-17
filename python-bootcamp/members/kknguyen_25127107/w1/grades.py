from statistics import median


def summary(scores: list[float]) -> dict:
    minimum = min(scores)
    maximum = max(scores)
    mean = round((sum(scores) / len(scores)), 2)
    med = round(median(scores), 2)

    result = {"min": minimum, "max": maximum, "mean": mean, "median": med}
    return result


print(summary([7.5, 9, 6, 8]))
