"""Module giao diện dòng lệnh (CLI) hỗ trợ lên kế hoạch công việc."""

import argparse
import sys
from datetime import date

from .io_utils import load_tasks


def main() -> None:
    """Khởi chạy ứng dụng CLI để đọc, sắp xếp và gợi ý danh sách công việc."""
    parser = argparse.ArgumentParser(description="Task planner CLI")
    parser.add_argument("file", help="Path to the tasks CSV file")
    parser.add_argument(
        "--hours", type=float, required=True, help="Available hours"
    )
    parser.add_argument(
        "--today",
        type=date.fromisoformat,
        default=None,
        help="Today's date in YYYY-MM-DD format",
    )

    args = parser.parse_args()
    today_date: date = args.today if args.today is not None else date.today()

    try:
        tasks = load_tasks(args.file)  #[cite: 1]
    except FileNotFoundError:
        print(f"Error: The file '{args.file}' was not found.", file=sys.stderr)
        sys.exit(1)
    except ValueError as exc:
        print(f"Error loading tasks: {exc}", file=sys.stderr)
        sys.exit(1)

    # Sắp xếp task theo deadline (days_left) tăng dần, sau đó độ quan trọng giảm dần[cite: 2]
    tasks.sort(
        key=lambda t: (t.days_left(today_date), -t.importance)
    )  #[cite: 2]

    selected_tasks = []
    accumulated_hours = 0.0

    for task in tasks:
        if accumulated_hours + task.effort_h <= args.hours:
            selected_tasks.append(task)
            accumulated_hours += task.effort_h

    print(f"Tonight ({accumulated_hours:.1f} h):")
    for i, task in enumerate(selected_tasks, 1):
        print(f"{i}. {task.title.ljust(15, '.')} {task.effort_h} h")


if __name__ == "__main__":
    main()
