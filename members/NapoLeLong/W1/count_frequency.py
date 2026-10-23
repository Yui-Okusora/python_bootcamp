def count_frequency(vector: list) -> dict:
    """Đếm số lần xuất hiện của từng phần tử trong một danh sách."""
    freq = {}
    for element in vector:
        if element in freq:
            freq[element] += 1
        else:
            freq[element] = 1
    return freq