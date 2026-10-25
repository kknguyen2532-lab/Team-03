# Study Planner CLI (`shared.study_planner`)

Công cụ dòng lệnh giúp lập kế hoạch học tập tối ưu dựa trên mức độ quan trọng (`importance`), thời lượng cần thiết (`effort_h`) và hạn chót (`deadline`) của từng công việc.

## 1. Kiến trúc luồng xử lý

Chương trình kết nối 4 module theo chuỗi xử lý tuần tự:
1. **`parse.py` (`parse_csv`)**: Đọc và kiểm tra tính hợp lệ của dữ liệu từ file CSV sang danh sách đối tượng `Task`.
2. **`prioritise.py` (`prioritise`)**: Sắp xếp danh sách công việc giảm dần theo độ ưu tiên `importance / max(days_left, 1)`.
3. **`allocate.py` (`allocate`)**: Phân bổ số giờ học hiện có (`hours`) cho các công việc theo chiến lược tham lam (greedy) tạo thành danh sách `Block`.
4. **`render.py` (`render`)**: Định dạng danh sách `Block` thành bảng kế hoạch dễ đọc trên terminal.

---

## 2. Cài đặt môi trường

Yêu cầu **Python 3.12+** (hoặc Python 3.10 trở lên). Từ thư mục gốc của repository, khởi tạo môi trường ảo và cài đặt các công cụ kiểm thử:

```bash
# Tạo và kích hoạt môi trường ảo (Windows)
python -m venv .venv
.venv\Scripts\activate

# Tạo và kích hoạt môi trường ảo (macOS / Linux)
python3 -m venv .venv
source .venv/bin/activate

# Cài đặt pytest và ruff
pip install pytest ruff