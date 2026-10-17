from typing import List, Any

def render(blocks: List[Any]) -> str:
    if not blocks:
        return "Chưa có kế hoạch nào được tạo."
    
    lines = ["=== BẢNG KẾ HOẠCH HỌC TẬP ==="]
    for idx, block in enumerate(blocks, start=1):
        if isinstance(block, dict):
            title = block.get("title", "Công việc không tên")
            effort = block.get("effort_h", 0)
            deadline = block.get("deadline", "Không có")
            lines.append(f"{idx}. [Task] {title} | Thời lượng: {effort}h | Hạn chót: {deadline}")
        elif hasattr(block, "title") and hasattr(block, "effort_h"):
            lines.append(f"{idx}. [Task] {block.title} | Thời lượng: {block.effort_h}h | Hạn chót: {block.deadline}")
        else:
            lines.append(f"{idx}. {str(block)}")
            
    return "\n".join(lines)