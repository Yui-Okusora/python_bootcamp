"""Điểm khởi chạy chương trình (Entry point) để kiểm tra nạp dữ liệu công việc."""

from pathlib import Path

from .io_utils import load_tasks


def main() -> None:
    """Đọc và hiển thị danh sách công việc từ file CSV mẫu."""
    csv_path = Path(__file__).resolve().parents[3] / "samples" / "tasks.csv"

    if not csv_path.exists():
        print(f"error: csv file {csv_path.name} not found")
        return

    try:
        tasks = load_tasks(csv_path)
        print(f"--- Loaded {len(tasks)} tasks ---")
        for task in tasks:
            print(task)
    except OSError as e:
        print(f"error: failed to read CSV file {csv_path.name}: {e}")


if __name__ == "__main__":
    main()