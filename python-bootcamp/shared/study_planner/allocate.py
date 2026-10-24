"""Greedy allocation of study hours to tasks."""

from shared.contract import Block, Task


def allocate(tasks: list[Task], hours: float) -> list[Block]:
    """Allocate available hours by importance, then deadline."""
    if hours <= 0 or not tasks:
        return []

    ordered_tasks = sorted(
        enumerate(tasks),
        key=lambda item: (
            -item[1].importance,
            item[1].deadline,
            item[0],
        ),
    )

    blocks: list[Block] = []
    remaining = hours

    for _, task in ordered_tasks:
        if remaining <= 0:
            break

        if task.effort_h <= 0:
            continue

        allocated = min(task.effort_h, remaining)

        blocks.append(Block(task=task, hours=allocated))
        remaining -= allocated

    return blocks
