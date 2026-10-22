"""Module cung cấp các công cụ phân tích và xử lý văn bản."""

import re
from collections import Counter


def word_count(text: str) -> dict[str, int]:
    """Đếm tần suất xuất hiện của từng từ trong đoạn văn bản.

    Args:
        text (str): Đoạn văn bản đầu vào.

    Returns:
        dict[str, int]: Tự điển ánh xạ từ từng từ sang số lần xuất hiện của nó.
    """
    words = re.findall(r"\b\w+\b", text.lower())
    return dict(Counter(words))


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    """Lấy danh sách k từ xuất hiện nhiều nhất trong văn bản.

    Sắp xếp theo thứ tự ưu tiên: Tần suất giảm dần, từ điển (alphabet) tăng dần.

    Args:
        text (str): Đoạn văn bản đầu vào.
        k (int): Số lượng từ top đầu cần lấy.

    Returns:
        list[tuple[str, int]]: Danh sách các cặp (từ, số_lần_xuất_hiện) có độ dài k.
    """
    word_counts = word_count(text)
    sorted_list = sorted(word_counts.items(), key=lambda item: (-item[1], item[0]))
    return sorted_list[:k]