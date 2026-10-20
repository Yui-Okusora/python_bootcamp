import argparse
from datetime import date
import sys
from shared.study_planner.allocate import allocate
from shared.study_planner.prioritise import prioritise
from shared.study_planner.render import render
from members.khoapham0112.w2.io_utils import load_tasks

"""write command-line tool for the w2 folder"""
def main() -> None:
    parser = argparse.ArgumentParser(
        description="Lập kế hoạch học tập từ file CSV."
    )

    parser.add_argument("path", help="Đường dẫn tới file CSV chứa công việc")
    parser.add_argument(
        "--hours",
        type=float,
        default=2.0,
        help="Số giờ học khả dụng: ",
    )
    parser.add_argument(
        "--today",
        type=lambda s: date.fromisoformat(s),
        default=date.today(),
        help="Ngày hiện tại YYYY-MM-DD (mặc định: hôm nay)",
    )

    args = parser.parse_args()
    try:
        tasks = load_tasks(args.path)
    except FileNotFoundError:
        print(
            f"Lỗi: Không tìm thấy file '{args.path}'. Vui lòng kiểm tra lại đường dẫn.",
            file=sys.stderr,
        )
        sys.exit(1)
    except Exception as e:
        print(f"Lỗi dữ liệu file: {e}", file=sys.stderr)
        sys.exit(1)

    sorted_tasks = prioritise(tasks, args.today)
    blocks = allocate(sorted_tasks, args.hours)
    plan_output = render(blocks)
    print(plan_output)


if __name__ == "__main__":
    main()