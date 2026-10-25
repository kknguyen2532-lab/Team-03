from collections import Counter, defaultdict


def analyse(pairs: list[tuple[str, int]]) -> dict:
    """
    Phân tích dữ liệu độ trễ của các route, tính toán số lượt gọi,
    độ trễ bách phân vị thứ 95 (p95) và xác định route chậm nhất.

    Args:
        pairs (list[tuple[str, int]]): Danh sách các tuple chứa tên route và độ trễ tương ứng.

    Returns:
        dict: Từ điển chứa kết quả phân tích bao gồm:
              - "counts": Số lượt xuất hiện của từng route.
              - "p95": Độ trễ bách phân vị 95 của từng route.
              - "slowest": Tên route có giá trị p95 cao nhất. Trả về None nếu danh sách rỗng.
    """
    if not pairs:
        return {"counts": {}, "p95": {}, "slowest": None}

    counts = Counter(route for route, latency in pairs)

    latencies_by_route = defaultdict(list)
    for route, latency in pairs:
        latencies_by_route[route].append(latency)

    p95 = {}
    for route, lats in latencies_by_route.items():
        sorted_lats = sorted(lats)

        index = int(0.95 * len(sorted_lats))

        if index >= len(sorted_lats):
            index = len(sorted_lats) - 1

        p95[route] = sorted_lats[index]

    slowest = max(p95, key=p95.get)

    return {"counts": dict(counts), "p95": p95, "slowest": slowest}
