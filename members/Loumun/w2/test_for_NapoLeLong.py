"""Module kiểm thử unit test cho hàm count_frequency."""

# ruff: noqa: N999
from typing import Any

import pytest

from members.NapoLeLong.W1.count_frequency import count_frequency


@pytest.mark.parametrize(
    "input_vector, expected",
    [
        ([], {}),
        ([5], {5: 1}),
        ([1, 2, 3], {1: 1, 2: 1, 3: 1}),
        ([1, 2, 2, 3, 3, 3], {1: 1, 2: 2, 3: 3}),
        (
            ["a", "b", "a", "c", "b", "a"],
            {"a": 3, "b": 2, "c": 1},
        ),
        ([-1, 0, -1, 2.5, 2.5], {-1: 2, 0: 1, 2.5: 2}),
    ],
)
def test_count_frequency_basic(
    input_vector: list[Any], expected: dict[Any, int]
) -> None:
    """Kiểm thử tính đúng đắn của count_frequency với các kiểu dữ liệu cơ bản."""
    assert count_frequency(input_vector) == expected


def test_count_frequency_with_tuples() -> None:
    """Kiểm thử count_frequency khi danh sách chứa các phần tử kiểu tuple."""
    vector = [(1, 2), (1, 2), (3, 4)]
    expected = {(1, 2): 2, (3, 4): 1}
    assert count_frequency(vector) == expected


def test_count_frequency_different_iterables() -> None:
    """Kiểm thử count_frequency làm việc với iterable dạng tuple."""
    assert count_frequency((1, 1, 2, 3, 3)) == {1: 2, 2: 1, 3: 2}


def test_count_frequency_unhashable_type() -> None:
    """Kiểm thử khả năng bắn ra lỗi TypeError khi truyền dữ liệu unhashable (list trong list)."""
    unhashable_vector = [[1, 2], [1, 2]]
    with pytest.raises(TypeError):
        count_frequency(unhashable_vector)