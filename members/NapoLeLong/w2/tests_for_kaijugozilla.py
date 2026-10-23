from kaijugozilla.W1.translate import merge_sorted_lists


def test_merge_standard() -> None:
    """Kiểm tra hợp nhất hai danh sách đã sắp xếp chuẩn."""
    assert merge_sorted_lists([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
def test_merge_different_lengths() -> None:
    """Kiểm tra hợp nhất hai danh sách có độ dài khác nhau."""
    assert merge_sorted_lists([1, 4], [2, 3, 5, 6]) == [1, 2, 3, 4, 5, 6]
def test_merge_with_empty_lists() -> None:
    """Kiểm tra hợp nhất khi có danh sách rỗng."""
    assert merge_sorted_lists([], [1, 2, 3]) == [1, 2, 3]
    assert merge_sorted_lists([4, 5, 6], []) == [4, 5, 6]
    assert merge_sorted_lists([], []) == []
def test_merge_with_duplicates() -> None:
    """Kiểm tra hợp nhất danh sách chứa các giá trị trùng lặp."""
    assert merge_sorted_lists([1, 2, 2], [2, 3, 4]) == [1, 2, 2, 2, 3, 4]
def test_merge_negative_numbers() -> None:
    """Kiểm tra hợp nhất danh sách có chứa số âm."""
    assert merge_sorted_lists([-5, -1, 3], [-3, 0, 4]) == [-5, -3, -1, 0, 3, 4]