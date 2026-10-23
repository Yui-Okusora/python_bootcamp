from pathlib import Path

from .io_utils import load_tasks


def main() -> None:
    """Chương trình chính để đọc và in danh sách công việc từ file CSV mẫu."""
    csv_path = Path(__file__).resolve().parents[3] / "samples" / "tasks.csv"
    if not csv_path.exists():
        print(f"Sample file not found at {csv_path}")
        return
    tasks = load_tasks(csv_path)
    print("=== LOADED TASKS ===")
    for t in tasks:
        print(t)

if __name__ == "__main__":
    main()