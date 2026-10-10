
import string


def word_count(text: str) -> dict[str, int]:
    text = text.lower()

    for char in string.punctuation:
        text = text.replace(char, " ")

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

    items.sort(key=lambda item: (-item[1], item[0]))

    if k <= 0:
        return []

    return items[:k]

print(word_count("Git is fun. Git is fast!"))
print(top_k("Git is fun. Git is fast!", 2))