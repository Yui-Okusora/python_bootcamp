from pathlib import Path
from .io_utils import load_tasks

def main():
    sample_path = Path(__file__).resolve().parents[3] / "samples" / "tasks_bad.csv"
    try:
        tasks = load_tasks(sample_path)
        print("Loaded tasks successfully:")
        for t in tasks:
            print(t)
    except Exception as e:
        print(f"Error loading tasks: {e}")

if __name__ == "__main__":
    main()