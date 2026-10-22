"""Module xử lý danh sách và loại bỏ các phần tử trùng lặp."""

from typing import TypeVar

T = TypeVar("T")


def remove_dupp(vector: list[T]) -> list[T]:
    """Loại bỏ các phần tử trùng lặp trong danh sách nhưng vẫn giữ nguyên thứ tự xuất hiện.

    Args:
        vector (list[T]): Danh sách các phần tử đầu vào.

    Returns:
        list[T]: Danh sách mới chỉ chứa các phần tử duy nhất theo thứ tự ban đầu.
    """
    seen: set[T] = set()
    result: list[T] = []
    for item in vector:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


if __name__ == "__main__":
    original_vector = ["apple", "banana", "apple", "orange"]
    unique_vector = remove_dupp(original_vector)
    print(unique_vector)