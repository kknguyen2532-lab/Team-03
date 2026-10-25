def summary(scores: list[float]) -> dict:
    """
    Tính toán các chỉ số thống kê cơ bản từ danh sách điểm số.

    Args:
        scores (list[float]): Danh sách các điểm số cần thống kê.

    Returns:
        dict: Từ điển chứa các giá trị bao gồm nhỏ nhất ("min"), lớn nhất ("max"),
              trung bình ("mean") và trung vị ("median").

    Raises:
        ValueError: Nếu danh sách điểm số đầu vào rỗng.
    """
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
