def can_register_thesis(credits: int, gpa: float) -> bool:
    """
    Kiểm tra điều kiện đăng ký khóa luận tốt nghiệp.

    Args:
        credits (int): Số tín chỉ tích lũy hiện tại.
        gpa (float): Điểm trung bình tích lũy (GPA).

    Returns:
        bool: True nếu đạt đủ điều kiện (tín chỉ >= 120 và GPA >= 2.0), ngược lại là False.
    """
    return credits >= 120 and gpa >= 2.0


def missing(credits: int, gpa: float) -> list[str]:
    """
    Xác định các điều kiện còn thiếu để được đăng ký khóa luận.

    Args:
        credits (int): Số tín chỉ tích lũy hiện tại.
        gpa (float): Điểm trung bình tích lũy (GPA).

    Returns:
        list[str]: Danh sách các lý do chưa đạt điều kiện (thiếu tín chỉ hoặc GPA thấp).
    """
    reasons = []
    if credits <= 120:
        reasons.append(f"need {120 - credits} more credits")
    if gpa < 2.0:
        reasons.append("gpa below 2.0")

    return reasons
