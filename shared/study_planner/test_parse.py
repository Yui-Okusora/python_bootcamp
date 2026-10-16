import csv
from datetime import date
from shared.contract import Task


def parse_csv(path: str) -> list[Task]:
    """Read a CSV file with header (title,importance,effort_h,deadline) 
    and return a list of Task objects.
    
    Raises ValueError with line number if any row is invalid.
    """
    tasks = []
    with open(path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                task = Task(
                    title=row["title"].strip(),
                    importance=int(row["importance"]),
                    effort_h=float(row["effort_h"]),
                    deadline=date.fromisoformat(row["deadline"].strip()),
                )
                tasks.append(task)
            except (ValueError, KeyError, AttributeError) as e:
                raise ValueError(f"Invalid row at line {reader.line_num}: {e}")
                
        return tasks


if __name__ == "__main__":
    import tempfile
    import os

    with tempfile.NamedTemporaryFile(mode="w", delete=False, encoding="utf-8", suffix=".csv") as tmp:
        tmp.write("title,importance,effort_h,deadline\n")
        tmp.write("Math Exam,5,3.5,2026-11-10\n")
        tmp.write("Physics Lab,3,2.0,2026-11-12\n")
        tmp_path = tmp.name

    try:
        # Kiểm tra đọc file hợp lệ
        tasks = parse_csv(tmp_path)
        assert len(tasks) == 2, f"Waiting for 2 task, task collected: {len(tasks)}"
        assert tasks[0].title == "Math Exam"
        assert tasks[0].importance == 5
        assert tasks[0].effort_h == 3.5
        assert tasks[0].deadline == date(2026, 11, 10)
        print("Test 1 (Valid): Success!")
    except Exception as e:
        print(f"Test 1 Failed: {e}")
    finally:
        os.remove(tmp_path)

    with tempfile.NamedTemporaryFile(mode="w", delete=False, encoding="utf-8", suffix=".csv") as tmp_err:
        tmp_err.write("title,importance,effort_h,deadline\n")
        tmp_err.write("Bad Task,10,1.5,2026-11-10\n")
        tmp_err_path = tmp_err.name

    try:
        parse_csv(tmp_err_path)
        print("Test 2 (ValueError): Failed")
    except ValueError as e:
        print(f"Test 2 (ValueError): Success!: {e}")
    finally:
        os.remove(tmp_err_path)