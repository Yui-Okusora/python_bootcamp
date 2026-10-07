import re
from collections import Counter

def word_count(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return dict(Counter(words))
def top_k(text, k):
    word_counts = word_count(text)
    sorted_list = dict(sorted(word_counts.items(), key=lambda item: (-item[1], item[0])))
    first_k = list(sorted_list.items())[:k]
    return first_k

    
