#ruff: noqa: DTZ005 
import argparse
import sys
from datetime import date, datetime
from pathlib import Path

from members.NapoLeLong.w2.io_utils import load_tasks
from shared.study_planner.allocate import allocate
from shared.study_planner.prioritise import prioritise
from shared.study_planner.render import render


def main() -> None:
    """Chạy công cụ dòng lệnh (CLI) để lập kế hoạch học tập từ file CSV."""
    parser = argparse.ArgumentParser(description="Task CLI Planner")

    parser.add_argument("path", type=str, help="Đường dẫn tới file CSV chứa công việc")
    parser.add_argument(
        "--hours",
        type=float,
        required=True,
        help="Số giờ học khả dụng",
    )
    parser.add_argument(
        "--today",
        type=lambda s: date.fromisoformat(s),
        default=datetime.now(),
        help="Ngày hiện tại YYYY-MM-DD (mặc định: hôm nay)",
    )

    args = parser.parse_args()
    
    csv_path = Path(args.path)
    if not csv_path.exists():
        fallback_path = Path(__file__).resolve().parents[3] / "samples" / args.path
        if fallback_path.exists():
            csv_path = fallback_path
        else:
            print(f"Lỗi: Không tìm thấy file tại '{args.path}'.", file=sys.stderr)
            sys.exit(1)

    try:
        tasks = load_tasks(str(csv_path))
    except ValueError as e:
        print(f"Lỗi dữ liệu file: {e}", file=sys.stderr)
        sys.exit(1)

    sorted_tasks = prioritise(tasks, args.today)
    blocks = allocate(sorted_tasks, args.hours)
    plan_output = render(blocks)
    
    print(plan_output)

if __name__ == "__main__":
    main()