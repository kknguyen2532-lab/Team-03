"""Date parsing utility using standard library datetime."""

from datetime import date, timedelta
import re

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
    """Parse relative or absolute date strings into a date object.

    Accepts:
      - 'YYYY-MM-DD' (e.g. '2026-10-30')
      - 'tomorrow'
      - 'in X days' (e.g. 'in 3 days')
      - Day of week abbreviation (e.g. 'Fri') for the next occurrence.
    Raises ValueError on unrecognized input.
    """
    clean_text = text.strip().lower()

    try:
        return date.fromisoformat(clean_text)
    except ValueError:
        pass

    if clean_text == "tomorrow":
        return today + timedelta(days=1)

    match_days = re.fullmatch(r"in\s+(\d+)\s+days?", clean_text)
    if match_days:
        days = int(match_days.group(1))
        return today + timedelta(days=days)

    if clean_text in WEEKDAYS:
        target_weekday = WEEKDAYS[clean_text]
        current_weekday = today.weekday()
        days_ahead = (target_weekday - current_weekday) % 7
        if days_ahead == 0:
            days_ahead = 7
        return today + timedelta(days=days_ahead)

    raise ValueError(f"Unknown date format: {text}")
