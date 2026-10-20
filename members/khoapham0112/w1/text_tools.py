import re
from collections import Counter

"""count different word in the sentence."""
def word_count(text: str) -> dict:
    words = re.findall(r'\b\w+\b', text.lower())
    return dict(Counter(words))
"""return the first k words that appear most in the sentence"""
def top_k(text: str, k: int) -> list:
    word_counts = word_count(text)
    sorted_list = dict(sorted(word_counts.items(), key=lambda item: (-item[1], item[0])))
    first_k = list(sorted_list.items())[:k]
    return first_k

    
