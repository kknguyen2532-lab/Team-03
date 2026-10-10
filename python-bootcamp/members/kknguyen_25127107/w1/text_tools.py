def word_count(text: str) -> dict[str,int]:
  text = text.lower()
  text = text.translate(str.maketrans("","",".,!?;:"))
  words = text.split()

  result = {}

  for word in words:
    if word in result:
      result[word] += 1
    else:
      result[word] = 1

  return result

def top_k(text: str, k: int) -> list[tuple[str,int]]:
  counts = word_count(text)

  result = list(counts.items())
  result.sort()

  result.sort(key=lambda item: item[1], reverse=True)

  return result[:k]


print(word_count("Git is fun. Git is fast!"))
print(top_k("Git is fun. Git is fast!", 2))