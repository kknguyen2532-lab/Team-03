from datetime import date, timedelta


def parse_due(text: str, today: date) -> date:
    """
    Chuyển đổi chuỗi văn bản ngày tháng thành đối tượng date.

    Hỗ trợ các định dạng:
    - "tomorrow": Ngày mai.
    - "in X days": X ngày sau (ví dụ: "in 3 days").
    - Thứ trong tuần viết tắt 3 chữ cái (vd: "mon", "tue"): Ngày thứ đó của tuần tiếp theo.
    - Định dạng ISO 8601 ("YYYY-MM-DD").

    Args:
        text (str): Chuỗi chứa thông tin ngày tháng cần phân tích.
        today (date): Ngày hiện tại làm mốc để tính toán các ngày tương đối.

    Returns:
        date: Đối tượng date tương ứng với chuỗi đầu vào.

    Raises:
        ValueError: Nếu chuỗi không khớp với bất kỳ định dạng nào được hỗ trợ.
    """
    text_lower = text.strip().lower()

    if text_lower == "tomorrow":
        return today + timedelta(days=1)

    if text_lower.startswith("in ") and text_lower.endswith(" days"):
        try:
            days = int(text_lower[3:-5].strip())
            return today + timedelta(days=days)
        except ValueError:
            pass

    weekdays = {"mon": 0, "tue": 1, "wed": 2, "thu": 3, "fri": 4, "sat": 5, "sun": 6}
    if text_lower in weekdays:
        target_wd = weekdays[text_lower]
        current_wd = today.weekday()

        days_ahead = target_wd - current_wd
        if days_ahead <= 0:
            days_ahead += 7

        return today + timedelta(days=days_ahead)

    try:
        return date.fromisoformat(text.strip())
    except ValueError:
        pass

    raise ValueError(f"Unknown date format: {text}")
