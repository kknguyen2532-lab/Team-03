import string

def word_count(text: str) -> dict[str, int]:
    """Count the occurrences of each word in the text (lower-case, ignoring punctuation)."""
    translator = str.maketrans("", "", string.punctuation)
    cleaned_text = text.translate(translator).lower()
    words = cleaned_text.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1

    return counts

def top_k(text: str, k: int) -> list[tuple[str, int]]:
    """Return top k most frequent words sorted by count descending, then alphabetically ascending."""
    counts = word_count(text)
    sorted_words = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    return sorted_words[:k]