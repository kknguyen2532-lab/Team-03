def word_count(text: str) -> dict[str, int]:
    text = text.lower()
    for char in ".,!?:;":
        text.replace(char, " ")
    words = text.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


def sort_by_word(item):
    return item[0]


def sort_by_count(item):
    return item[1]


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    counts = word_count(text)
    result = list(counts.items())

    result.sort(key=sort_by_word)
    result.sort(key=sort_by_count, reverse=True)

    return result[:k]


print(top_k("Git is fun. Git is fast!", 2))
