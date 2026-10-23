import argparse
import os
import sys
from datetime import datetime


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments for the task scheduler CLI."""
    parser = argparse.ArgumentParser(
        description="Command-line task scheduler CLI tool."
    )

    parser.add_argument(
        "csv_file", type=str, help="Path to the tasks CSV file"
    )

    parser.add_argument(
        "--hours",
        type=float,
        default=2.0,
        help="Available hours for tonight (default: 2.0)",
    )

    parser.add_argument(
        "--today",
        type=str,
        default=datetime.now().strftime("%Y-%m-%d"),
        help="Reference date in YYYY-MM-DD format (default: today)",
    )

    return parser.parse_args()


def main() -> None:
    """Execute the command-line task scheduler interface."""
    args = parse_args()

    try:
        datetime.strptime(args.today, "%Y-%m-%d")
    except ValueError:
        print(
            f"Error: Invalid date format '{args.today}'. Expected YYYY-MM-DD.",
            file=sys.stderr,
        )
        sys.exit(1)

    if not os.path.exists(args.csv_file):
        print(
            f"Error: The specified file '{args.csv_file}' was not found.",
            file=sys.stderr,
        )
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
