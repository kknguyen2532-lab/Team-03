def word_count(text: str) -> dict[str, int]:
    for p in ".,!?:;":
        text = text.replace(p, "")
    words = text.lower().split()
    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1
    return counts

def top_k(text: str, k: int) -> list[tuple[str, int]]:
    counts = word_count(text)
    return sorted(counts.items(), key=lambda x: (-x[1], x[0]))[:k]