
"""Shared data models for the study planner."""

from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    """Represent a task in the study planner."""
    """A study task read from a CSV file."""

    title: str
    importance: int
    effort_h: float
    deadline: date


@dataclass
class Block:
    """Represent a scheduled block of study time."""
    """A task and the amount of time allocated to it."""

    task: Task
    hours: float
