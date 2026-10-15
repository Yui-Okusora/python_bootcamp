from pathlib import Path
from .io_utils import load_tasks


def main():
    project_root = Path(__file__).resolve().parent.parent.parent.parent
    csv_path = project_root / "samples" / "tasks.csv"

    try:
        tasks = load_tasks(str(csv_path))
        print(f"Loaded {len(tasks)} tasks:\n")
        for task in tasks:
            print(task)
    except Exception as e:
        print(f"Error loading tasks: {e}")


if __name__ == "__main__":
    main()