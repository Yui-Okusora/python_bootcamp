from pathlib import Path
from .io_utils import load_tasks


def main():
    current_dir = Path(__file__).parent
    csv_path = current_dir / "tasks.csv"

    try:
        tasks = load_tasks(str(csv_path))

        print(f"=== ĐÃ TẢI {len(tasks)} TASK TỪ CSV ===")
        for task in tasks:
            print(task)

    except Exception as e:
        print(f"Lỗi khi tải file CSV: {e}")


if __name__ == "__main__":
    main()