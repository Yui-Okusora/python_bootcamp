"""Module kiểm thử End-to-End (E2E) cho ứng dụng study_planner CLI."""

from pathlib import Path
import subprocess


def test_study_planner_e2e(tmp_path: Path) -> None:
    """Kiểm thử E2E quy trình đọc file CSV và lập kế hoạch theo thời gian khả dụng."""
    # 1. Lấy file csv
    csv_file = Path("./samples/tasks.csv")
    # 2. Gọi lệnh CLI như một subprocess
    cmd = [
        "python",
        "-m",
        "shared.study_planner",
        str(csv_file),
        "--hours",
        "2",
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)

    # 3. Kiểm tra kết quả
    assert (
        result.returncode == 0
    ), f"Command failed with error: {result.stderr}"

    # Assignment (1.5h) và DS exam (0.5h) vừa đủ 2.0h nên sẽ được in ra
    assert "Assignment" in result.stdout 
    assert "DS exam" in result.stdout

    # Task "Read chapter 3" vượt quá thời lượng 2h nên sẽ không xuất hiện
    assert "Read chapter 3" not in result.stdout 


def test_study_planner_missing_file() -> None:
    """Kiểm thử trường hợp CLI xử lý lỗi file CSV không tồn tại."""
    cmd = [
        "python",
        "-m",
        "shared.study_planner",
        "non_existent_file.csv",
        "--hours",
        "2",
    ]  #[cite: 15]

    result = subprocess.run(cmd, capture_output=True, text=True)

    # Lệnh sẽ trả về code lỗi (thường là 1) khi file không tồn tại
    assert result.returncode != 0
