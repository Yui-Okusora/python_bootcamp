import argparse
import sys
from datetime import date

from shared.study_planner.allocate import allocate
from shared.study_planner.parse import parse_csv
from shared.study_planner.prioritise import prioritise
from shared.study_planner.render import render


def build_parser() -> argparse.ArgumentParser:
    """Xây dựng và trả về đối tượng phân tích tham số dòng lệnh cho study_planner."""
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
    """Hàm thực thi chính tích hợp 4 module trong study_planner với đầy đủ xử lý lỗi."""
    parser = build_parser()
    args = parser.parse_args()

    try:
        tasks = parse_csv(args.path)
        if not tasks:
            print("Error: File công việc trống.", file=sys.stderr)
            sys.exit(1)

        sorted_tasks = prioritise(tasks, args.today)
        
        # Hàm allocate sẽ tự động cắt/phân bổ các task vừa khít với số giờ --hours cho phép
        blocks = allocate(sorted_tasks, args.hours)
        plan_output = render(blocks)
        
        if plan_output:
            print(plan_output)

    except FileNotFoundError:
        print(f"Error: Không tìm thấy file tại đường dẫn '{args.path}'.", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()