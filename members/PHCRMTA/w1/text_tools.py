def word_count(text: str) -> dict[str, int]:
    text = text.lower()
    
    punctuation = ".,!?;:"
    for char in punctuation:
        text = text.replace(char, "")
        
    words = text.split()
    
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
            
    return counts


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    counts = word_count(text)
    
    items = list(counts.items())
    
    sorted_items = sorted(items, key=lambda x: (-x[1], x[0]))
    
    return sorted_items[:k]