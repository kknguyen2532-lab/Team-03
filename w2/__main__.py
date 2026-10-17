import os
from .io_utils import load_tasks

def main():
    sample_path = os.path.join(os.path.dirname(__file__), "sample.csv")
    
    if not os.path.exists(sample_path):
        with open(sample_path, "w", encoding="utf-8") as f:
            f.write("title,importance,effort_h,deadline\n")
            f.write("DS exam,5,6,2026-10-30\n")
            f.write("Assignment,4,1.5,2026-10-27\n")

    print(f"Đang đọc dữ liệu từ: {sample_path}")
    try:
        tasks = load_tasks(sample_path)
        print(f"Đã load thành công {len(tasks)} tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"  {idx}. {task}")
    except Exception as e:  # noqa: BLE001
        print(f"Lỗi: {e}")

if __name__ == "__main__":
    main()