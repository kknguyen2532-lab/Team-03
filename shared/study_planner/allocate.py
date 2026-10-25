from shared.contract import Task, Block
from shared.study_planner.errors import InfeasiblePlan

def allocate(tasks: list[Task], hours: float) -> list[Block]:
    total_effort = sum(task.effort_h for task in tasks)
    
    if total_effort > hours:
        raise InfeasiblePlan(f"Kế hoạch không khả thi: Cần {total_effort}h nhưng chỉ có {hours}h.")
    
    blocks = []
    for task in tasks:
        blocks.append(Block(task=task, hours=task.effort_h))
    return blocks
