"""Date parsing utilities for Week 3 homework (W3-1)."""

from datetime import date, timedelta
import re

_WEEKDAYS: dict[str, int] = {
    "mon": 0,
    "monday": 0,
    "tue": 1,
    "tuesday": 1,
    "wed": 2,
    "wednesday": 2,
    "thu": 3,
    "thursday": 3,
    "fri": 4,
    "friday": 4,
    "sat": 5,
    "saturday": 5,
    "sun": 6,
    "sunday": 6,
}

_ISO_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
_IN_DAYS_RE = re.compile(r"^in\s+(\d+)\s+days?$", re.IGNORECASE)


def parse_due(text: str, today: date) -> date:
    """Parse a human-friendly due date string relative to `today`.

    Supported formats:
    - ISO date: "YYYY-MM-DD" (e.g., "2026-10-30")
    - "tomorrow"
    - "in <N> days" (e.g., "in 3 days")
    - Weekday name: "Mon".."Sun" (next occurrence strictly after `today`)
    """
    if not isinstance(text, str):
        raise ValueError("Due date text must be a string")

    cleaned = text.strip()
    if not cleaned:
        raise ValueError("Due date text cannot be empty")

    # 1. Định dạng chuẩn YYYY-MM-DD
    if _ISO_DATE_RE.match(cleaned):
        return date.fromisoformat(cleaned)

    lowered = cleaned.lower()

    # 2. Định dạng "tomorrow"
    if lowered == "tomorrow":
        return today + timedelta(days=1)

    # 3. Định dạng "in N days"
    match = _IN_DAYS_RE.match(lowered)
    if match:
        days = int(match.group(1))
        if days <= 0:
            raise ValueError("Number of days must be positive")
        return today + timedelta(days=days)

    # 4. Tên thứ trong tuần (lần xuất hiện tiếp theo)
    if lowered in _WEEKDAYS:
        target_wd = _WEEKDAYS[lowered]
        days_ahead = (target_wd - today.weekday()) % 7
        if days_ahead == 0:
            days_ahead = 7
        return today + timedelta(days=days_ahead)

    raise ValueError(f"Unknown due date format: {text!r}")