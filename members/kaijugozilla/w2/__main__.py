from pathlib import Path

from .io_utils import load_tasks


def main() -> None:
    csv_path = (
        Path(__file__).resolve().parents[3]
        / "samples"
        / "tasks.csv"
    )

    tasks = load_tasks(csv_path)

    for task in tasks:
        print(task)


if __name__ == "__main__":
    main()
