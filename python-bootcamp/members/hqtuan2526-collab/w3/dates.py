
import re
from datetime import date, timedelta


WEEKDAYS = {
    "mon": 0,
    "tue": 1,
    "wed": 2,
    "thu": 3,
    "fri": 4,
    "sat": 5,
    "sun": 6,
}


def parse_due(text: str, today: date) -> date:
    """Parse a due date from ISO date, relative text, or weekday."""
    value = text.strip().lower()

    if not value:
        raise ValueError("Due date cannot be empty.")

    try:
        return date.fromisoformat(value)
    except ValueError:
        pass

    if value == "tomorrow":
        return today + timedelta(days=1)

    match = re.fullmatch(r"in\s+(\d+)\s+days?", value)
    if match:
        days = int(match.group(1))
        return today + timedelta(days=days)

    if value in WEEKDAYS:
        target_day = WEEKDAYS[value]
        days_ahead = (target_day - today.weekday()) % 7

        if days_ahead == 0:
            days_ahead = 7

        return today + timedelta(days=days_ahead)

    raise ValueError(f"Unknown due date: {text}")
