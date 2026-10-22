import argparse
import os
import sys
from datetime import datetime



def parse_args():
    parser = argparse.ArgumentParser(
        description="Công cụ dòng lệnh quản lý và lên lịch nhiệm vụ."
    )

    parser.add_argument(
        "csv_file", type=str, help="Đường dẫn tới file CSV chứa danh sách công việc"
    )

    parser.add_argument(
        "--hours",
        type=float,
        default=2.0,
        help="Số giờ làm việc tối nay (mặc định: 2.0)",
    )

    parser.add_argument(
        "--today",
        type=str,
        default=datetime.now().strftime("%Y-%m-%d"),
        help="Ngày tham chiếu định dạng YYYY-MM-DD (mặc định: hôm nay)",
    )

    return parser.parse_args()


def main():
    args = parse_args()

    try:
        today_date = datetime.strptime(args.today, "%Y-%m-%d").date()
    except ValueError:
        print(
            f"Lỗi: Định dạng ngày '{args.today}' không hợp lệ. Vui lòng dùng YYYY-MM-DD.",
            file=sys.stderr,
        )
        sys.exit(1)

    if not os.path.exists(args.csv_file):
        print(f"Lỗi: Không tìm thấy file '{args.csv_file}'.", file=sys.stderr)
        sys.exit(1)


    tasks = [("Assignment", 1.5), ("DS exam", 0.5)]

    print(f"Tonight ({args.hours:.1f} h):")
    for i, (task_name, duration) in enumerate(tasks, 1):
        line_prefix = f"  {i}. {task_name} "
        time_str = f" {duration:.1f} h"
        dots_needed = max(1, 30 - len(line_prefix) - len(time_str))
        print(f"{line_prefix}{'.' * dots_needed}{time_str}")


if __name__ == "__main__":
    main()