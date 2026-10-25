import string
from collections import Counter


def word_count(text: str) -> dict[str, int]:
    """
    Đếm số lượng từ trong văn bản, bỏ qua dấu câu và không phân biệt chữ hoa chữ thường.

    Args:
        text (str): Đoạn văn bản đầu vào.

    Returns:
        dict[str, int]: Từ điển chứa tần suất xuất hiện của các từ, được sắp xếp giảm dần 
                        theo số lượng và tăng dần theo thứ tự từ điển (alphabet).
    """
    clean_text = text.lower()
    for p in string.punctuation:
        clean_text = clean_text.replace(p, " ")

    words = clean_text.split()
    counts = Counter(words)
    return dict(sorted(counts.items(), key=lambda x: (-x[1], x[0])))


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    """
    Trích xuất danh sách k từ xuất hiện nhiều nhất trong văn bản.

    Args:
        text (str): Đoạn văn bản đầu vào.
        k (int): Số lượng từ phổ biến nhất cần lấy.

    Returns:
        list[tuple[str, int]]: Danh sách chứa tối đa k tuple gồm (từ, số lượng), 
                               đã được sắp xếp theo tần suất xuất hiện.
    """
    counts = word_count(text)
    return list(counts.items())[:k]