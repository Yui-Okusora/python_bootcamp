"""Module kiểm thử End-to-End (E2E) cho ứng dụng study_planner CLI."""

from pathlib import Path
import subprocess


def test_study_planner_e2e(tmp_path: Path) -> None:
    """Kiểm thử E2E quy trình đọc file CSV và lập kế hoạch theo thời gian khả dụng."""
    # 1. Tạo file CSV mẫu giả lập trực tiếp trong thư mục tạm (tmp_path) của pytest[cite: 15]
    sample_csv = tmp_path / "tasks.csv"
    sample_csv.write_text(
        "title,importance,effort,deadline\n"
        "Assignment,5,1.5,2026-10-27\n"
        "DS exam,4,0.5,2026-10-27\n"
        "Read chapter 3,3,1.0,2026-10-30\n",
        encoding="utf-8",
    )  #[cite: 15]

    # 2. Gọi lệnh CLI như một subprocess[cite: 15]
    cmd = [
        "python",
        "-m",
        "shared.study_planner",
        str(sample_csv),
        "--hours",
        "2",
    ]  #[cite: 15]

    result = subprocess.run(cmd, capture_output=True, text=True)  #[cite: 15]

    # 3. Kiểm tra kết quả[cite: 15]
    assert (
        result.returncode == 0
    ), f"Command failed with error: {result.stderr}"  #[cite: 15]

    # Assignment (1.5h) và DS exam (0.5h) vừa đủ 2.0h nên sẽ được in ra[cite: 15]
    assert "Assignment" in result.stdout  #[cite: 15]
    assert "DS exam" in result.stdout  #[cite: 15]

    # Task "Read chapter 3" vượt quá thời lượng 2h nên sẽ không xuất hiện[cite: 15]
    assert "Read chapter 3" not in result.stdout  #[cite: 15]


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

    result = subprocess.run(cmd, capture_output=True, text=True)  #[cite: 15]

    # Lệnh sẽ trả về code lỗi (thường là 1) khi file không tồn tại[cite: 15]
    assert result.returncode != 0  #[cite: 15]