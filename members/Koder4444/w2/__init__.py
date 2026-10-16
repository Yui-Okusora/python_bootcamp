from members.Koder4444.w2.errors import InfeasiblePlan, check_feasible
from members.Koder4444.w2.io_utils import load_tasks, save_json
from members.Koder4444.w2.models import Task

__all__ = ["InfeasiblePlan", "Task", "check_feasible", "load_tasks", "save_json"]


def main() -> None:
    import os

    # Đường dẫn tới file CSV mẫu (giả sử bạn để file mẫu trong thư mục w2 hoặc gốc)
    csv_path = os.path.join(os.path.dirname(__file__), "tasks.csv")
    
    if os.path.exists(csv_path):
        print(f"Loading tasks from {csv_path}...")
        tasks = load_tasks(csv_path)
        for t in tasks:
            print(t)
    else:
        print(f"Sample CSV file not found at {csv_path}. Please ensure tasks.csv exists.")


if __name__ == "__main__":
    main()