import argparse
import sys
from datetime import date
from shared.study_planner.parse import parse_csv
from shared.study_planner.prioritise import prioritise
from shared.study_planner.allocate import allocate
from shared.study_planner.render import render

def main() -> None:
    """Run the study planner CLI to parse tasks, allocate hours, and print the schedule."""
    parser = argparse.ArgumentParser(
        description="Study planner command-line tool"
    )

    parser.add_argument("path", help="Path to the tasks CSV file")
    parser.add_argument(
        "--hours",
        type=float,
        default=2.0,
        help="Available study hours",
    )
    parser.add_argument(
        "--today",
        type=date.fromisoformat,
        default=date.today(),
        help="Current date in YYYY-MM-DD format",
    )

    args = parser.parse_args()

    try:
        tasks = parse_csv(args.path)
    except FileNotFoundError:
        sys.exit(1)
    except ValueError:
        sys.exit(1)

    sorted_tasks = prioritise(tasks, args.today)
    blocks = allocate(sorted_tasks, args.hours)
    plan_output = render(blocks)
    print(plan_output)

if __name__ == "__main__":
    main()