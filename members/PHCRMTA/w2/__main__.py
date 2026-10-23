from pathlib import Path

from .io_utils import load_tasks


def main() -> None:
    """Run the main entry point to load and display tasks."""
    project_root = Path(__file__).resolve().parent.parent.parent.parent
    csv_path = project_root / "samples" / "tasks.csv"

    try:
        tasks = load_tasks(str(csv_path))
        print(f"Loaded {len(tasks)} tasks:\n")
        for task in tasks:
            print(task)
    except Exception as e: # noqa: BLE001
        print(f"Error loading tasks: {e}")


if __name__ == "__main__":
    main()