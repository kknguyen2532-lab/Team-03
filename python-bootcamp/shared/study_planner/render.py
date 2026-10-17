
from typing import Any


def render(blocks: list[Any]) -> str:
    if not blocks:
        return "Chưa có kế hoạch nào được tạo."

    lines = ["=== BẢNG KẾ HOẠCH HỌC TẬP ==="]

    for idx, block in enumerate(blocks, start=1):
        if isinstance(block, dict):
            title = block.get("title", "Công việc không tên")
            effort = block.get("effort_h", 0)
            deadline = block.get("deadline", "Không có")

            lines.append(
                f"{idx}. [Task] {title} | "
                f"Thời lượng: {effort}h | Hạn chót: {deadline}"
            )
        elif hasattr(block, "title") and hasattr(block, "effort_h"):
            lines.append(
                f"{idx}. [Task] {block.title} | "
                f"Thời lượng: {block.effort_h}h | "
                f"Hạn chót: {getattr(block, 'deadline', 'Không có')}"
            )
        else:
            lines.append(f"{idx}. {block!s}")

    return "\n".join(lines)
