from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    title: Python_Week2
    importance: 4  # 1-5
    effort_h: 4
    deadline: 17/10/2026


@dataclass
class Block:
    task: Homework
    hours: 3