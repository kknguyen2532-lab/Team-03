from shared.contract import Block


def render(blocks: list[Block]) -> str:
    """Return a human-readable study plan."""
    if not blocks:
        return "Chưa có kế hoạch nào được tạo."

    lines = ["=== BẢNG KẾ HOẠCH HỌC TẬP ==="]

    for index, block in enumerate(blocks, start=1):
        task = block.task
        lines.append(
            f"{index}. {task.title} | "
            f"Thời lượng phân bổ: {block.hours:g}h | "
            f"Hạn chót: {task.deadline.isoformat()}"
        )

    return "\n".join(lines)
