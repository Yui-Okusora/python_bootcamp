
import argparse
from datetime import date
import sys

from shared.study_planner.allocate import allocate
from shared.study_planner.parse import parse_csv
from shared.study_planner.prioritise import prioritise
from shared.study_planner.render import render


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Lập kế hoạch học tập tự động từ file công việc CSV."
    )

    parser.add_argument("path", help="Đường dẫn tới file CSV chứa danh sách công việc")

    parser.add_argument(
        "--hours",
        type=float,
        default=0.0,
        help="Số giờ khả dụng để học tập",
    )

    parser.add_argument(
        "--today",
        type=lambda s: date.fromisoformat(s),
        default=date.today(),
        help="Ngày hiện tại theo định dạng YYYY-MM-DD (mặc định: hôm nay)",
    )

    return parser


def main() -> None:
    """Hàm thực thi chính tích hợp 4 module trong study_planner."""
    parser = build_parser()
    args = parser.parse_args()

    try:
        tasks = parse_csv(args.path)
    except FileNotFoundError:
        print(
            f"Error: Missing file '{args.path}'. Please check the path.",
            file=sys.stderr,
        )
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file '{args.path}': {e}", file=sys.stderr)
        sys.exit(1)

    sorted_tasks = prioritise(tasks, args.today)

    blocks = allocate(sorted_tasks, args.hours)

    plan_output = render(blocks)
    if plan_output:
        print(plan_output)


if __name__ == "__main__":
    main()