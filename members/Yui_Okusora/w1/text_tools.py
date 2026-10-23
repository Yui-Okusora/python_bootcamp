def word_count(text: str) -> dict[str, int]:
    """Count the frequency of each word in text after removing punctuation and lowercasing."""
    punctuation = ".,!?:;"
    lowercased = text.lower()

    cleaned_chars: list[str] = []
    for i in range(len(lowercased)):
        char = lowercased[i]
        if char not in punctuation:
            cleaned_chars.append(char)

    cleaned_text = "".join(cleaned_chars)
    words = cleaned_text.split()
    counts: dict[str, int] = {}

    for i in range(len(words)):
        word = words[i]
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    """Return the top k most frequent words sorted by frequency (descending) then alphabetically."""
    counts = word_count(text)
    items = list(counts.items())

    items.sort(key=lambda item: (-item[1], item[0]))

    result: list[tuple[str, int]] = []
    limit = min(k, len(items))
    for i in range(limit):
        result.append(items[i])

    return result