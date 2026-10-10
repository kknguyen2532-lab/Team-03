import string 
from collections import Counter

def word_count(text: str) -> dict[str, int]:
    clean_text = text.lower()
    for p in string.punctuation:
        clean_text = clean_text.replace(p, " ")

    words = clean_text.split()
    counts = Counter(words)
    return dict(sorted(counts.items(), key = lambda x: (-x[1], x[0])))

def top_k(text: str, k: int) -> list[tuple[str,int]]:
    counts = word_count(text)
    return list(counts.items())[:k]