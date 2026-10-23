import argparse
from datetime import date
from pathlib import Path
import sys

from ..w2.io_utils import load_tasks
from shared.study_planner.allocate import allocate
from shared.study_planner.prioritise import prioritise
from shared.study_planner.render import render


def main() -> None:
    parser = argparse.ArgumentParser(description="Study planner CLI tool")
    parser.add_argument("tasks_file", type=Path, help="Path to CSV file")
    parser.add_argument("--hours", type=float, required=True, help="Study hours available")
    parser.add_argument(
        "--today",
        type=date.fromisoformat,
        default=date.today(),
        help="Reference day in YYYY-MM-DD format (default: today)",
    )

    args = parser.parse_args()

    if not args.tasks_file.exists():
        print(f"Error: File '{args.tasks_file}' does not exist.", file=sys.stderr)
        sys.exit(1)

    try:
        tasks = load_tasks(args.tasks_file)

        try:
            prioritized_tasks = prioritise(tasks, today=args.today)
        except TypeError:
            prioritized_tasks = prioritise(tasks)

        allocated_plan = allocate(prioritized_tasks, hours=args.hours)
        output = render(allocated_plan)
        print(output)

    except Exception as err:
        print(f"Error processing plan: {err}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()