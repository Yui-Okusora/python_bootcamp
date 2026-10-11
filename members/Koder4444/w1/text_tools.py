from collections import Counter

def word_count(text: str) -> dict[str, int]: 
    translator = str.maketrans("", "", ",.?!;:")
    cleaned_text = text.lower().translate(translator)
    
    return dict(Counter(cleaned_text.split()))

def top_k(text: str, k: int) -> list[tuple[str, int]]:
    count = word_count(text)
    
    return sorted(count.items(), key=lambda x: (-x[1], x[0]))[:k]
    