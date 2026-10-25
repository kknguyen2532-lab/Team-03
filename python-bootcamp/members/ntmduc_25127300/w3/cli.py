import argparse
import sys
from datetime import date
from pathlib import Path

from shared.study_planner.allocate import allocate
from shared.study_planner.parse import parse_csv
from shared.study_planner.prioritise import prioritise


def main():
    """
    Giao diện dòng lệnh (CLI) chính của ứng dụng Study Planner.

    Sử dụng argparse để nhận các tham số đầu vào bao gồm: file dữ liệu CSV,
    số giờ khả dụng (--hours), và ngày hiện tại (--today).
    Hàm sẽ chạy chuỗi quy trình: đọc dữ liệu -> ưu tiên task -> phân bổ thời gian,
    sau đó in kế hoạch ra màn hình.

    Thoát chương trình với mã lỗi 1 (sys.exit(1)) nếu file không tồn tại,
    ngày sai định dạng, hoặc gặp lỗi trong quá trình phân tích dữ liệu.
    """
    parser = argparse.ArgumentParser(description="Study Planner CLI")

    parser.add_argument("file", help="Đường dẫn đến file CSV chứa danh sách task")
    parser.add_argument(
        "--hours", type=float, required=True, help="Số giờ bạn có thể học"
    )
    parser.add_argument(
        "--today",
        type=str,
        default=str(date.today()),
        help="Ngày hiện tại định dạng YYYY-MM-DD (mặc định là hôm nay)",
    )

    args = parser.parse_args()

    file_path = Path(args.file)
    if not file_path.is_file():
        print(f"Error: File '{args.file}' does not exist.", file=sys.stderr)
        sys.exit(1)

    try:
        today_date = date.fromisoformat(args.today)
    except ValueError:
        print("Error: --today phải có định dạng YYYY-MM-DD.", file=sys.stderr)
        sys.exit(1)

    try:
        tasks = parse_csv(file_path)

        prioritised_tasks = prioritise(tasks, today_date)

        blocks = allocate(prioritised_tasks, args.hours)

        print(
            f"Kế hoạch học tập cho ngày {today_date} (Tổng thời gian: {args.hours}h):"
        )
        for idx, block in enumerate(blocks, start=1):
            print(f"{idx}. {block.task.title} - {block.hours}h")

    except Exception as e:  # noqa: BLE001
        print(f"Lỗi trong quá trình xử lý dữ liệu: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
