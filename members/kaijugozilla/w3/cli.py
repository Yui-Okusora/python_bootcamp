import argparse
import sys
from datetime import date
from pathlib import Path

from ..w2.io_utils import load_tasks


def build_plan(tasks: list, available_h: float, today: date) -> str:
    """Prioritise tasks and assign the available study hours."""
    ordered = sorted(
        tasks,
        key=lambda task: (
            -task.importance / max((task.deadline - today).days, 1),
            task.deadline,
            task.title,
        ),
    )

    remaining = available_h
    lines = [f"Tonight ({available_h:.1f} h):"]
    position = 1

    for task in ordered:
        if remaining <= 0:
            break

        hours = min(task.effort_h, remaining)

        if hours <= 0:
            continue

        lines.append(
            f"  {position}. {task.title} ...... {hours:.1f} h"
        )
        position += 1
        remaining -= hours

    if len(lines) == 1:
        lines.append("  No tasks scheduled.")

    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    """Load tasks from CSV and print a study plan."""
    parser = argparse.ArgumentParser(
        description="Study planner for tonight"
    )

    parser.add_argument(
        "path",
        type=Path,
        help="Path to a tasks CSV file",
    )

    parser.add_argument(
        "--hours",
        type=float,
        required=True,
        help="Hours available",
    )

    parser.add_argument(
        "--today",
        help="Date in YYYY-MM-DD (default: today)",
    )

    args = parser.parse_args(argv)

    if args.hours < 0:
        parser.error("--hours must be non-negative")

    if args.today is None:
        today = date.today()
    else:
        try:
            today = date.fromisoformat(args.today)
        except ValueError:
            parser.error("--today must be in YYYY-MM-DD format")

    try:
        tasks = load_tasks(args.path)
    except FileNotFoundError:
        print(
            f"Error: file not found: {args.path}",
            file=sys.stderr,
        )
        return 1
    except ValueError as error:
        print(f"Error: invalid CSV data: {error}", file=sys.stderr)
        return 1

    print(build_plan(tasks, args.hours, today))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
