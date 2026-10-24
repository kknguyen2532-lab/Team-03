import re
from datetime import date, timedelta

WEEKDAYS = {
    "mon": 0, "monday": 0,
    "tue": 1, "tuesday": 1,
    "wed": 2, "wednesday": 2,
    "thu": 3, "thursday": 3,
    "fri": 4, "friday": 4,
    "sat": 5, "saturday": 5,
    "sun": 6, "sunday": 6,
}


def parse_due(text: str, today: date) -> date:
    """Convert a supported due-date expression into a date."""
    value = text.strip()

    if not value:
        raise ValueError("Due date cannot be empty")

    # Format: YYYY-MM-DD
    try:
        return date.fromisoformat(value)
    except ValueError:
        pass

    normalized = value.lower()

    if normalized == "tomorrow":
        return today + timedelta(days=1)

    # Formats: in 1 day, in 3 days, ...
    match = re.fullmatch(r"in\s+(\d+)\s+days?", normalized)
    if match:
        return today + timedelta(days=int(match.group(1)))

    # Weekday: the next occurrence strictly after today
    if normalized in WEEKDAYS:
        target_day = WEEKDAYS[normalized]
        days_ahead = (target_day - today.weekday()) % 7

        if days_ahead == 0:
            days_ahead = 7

        return today + timedelta(days=days_ahead)

    raise ValueError(f"Unknown due date: {text!r}")