def word_count(text: str) -> dict[str, int]:
    """Đếm tần suất xuất hiện của từng từ trong chuỗi văn bản (đã loại bỏ dấu câu)."""
    cleaned = text.lower().translate(str.maketrans('', '', '.,!?;:'))
    counts: dict[str, int] = {}
    for word in cleaned.split():
        counts[word] = counts.get(word, 0) + 1
    return counts
def top_k(text: str, k: int) -> list[tuple[str, int]]:
    """Trả về k từ xuất hiện nhiều nhất theo thứ tự ưu tiên tần suất giảm dần."""
    counts = word_count(text)
    return sorted(counts.items(), key=lambda x: (-x[1], x[0]))[:k]