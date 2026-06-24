"""
Bài 11. Nhiều nguồn (Multi-source Dijkstra)
Tìm với mỗi đỉnh khoảng cách tới nguồn gần nhất.
Gợi ý: thêm "siêu nguồn" nối tới mọi nguồn với trọng số 0.
"""
import heapq

def multi_source_dijkstra(n, adj, sources):
    """
    n: số đỉnh
    adj: danh sách kề adj[u] = [(v, w), ...]
    sources: tập đỉnh nguồn
    Trả về dist[i] = khoảng cách ngắn nhất từ i tới nguồn gần nhất
    """
    INF = float('inf')
    dist = [INF] * n

    # Siêu nguồn: khởi tạo tất cả nguồn với dist = 0
    heap = []
    for s in sources:
        dist[s] = 0
        heapq.heappush(heap, (0, s))

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))

    return dist


# --- Ví dụ: dùng đồ thị G1 (bài 1–8) ---
# Đỉnh 0–5, đồ thị có hướng
adj_G1 = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5), (4, 8)],
    3: [(4, 3), (5, 6)],
    4: [(5, 2)],
    5: []
}

n = 6
sources = {0, 3}
dist = multi_source_dijkstra(n, adj_G1, sources)

print("Multi-source Dijkstra — nguồn = {0, 3}")
print(f"{'Đỉnh':<8} {'dist (tới nguồn gần nhất)'}")
print("-" * 35)
for i in range(n):
    d = dist[i] if dist[i] != float('inf') else -1
    print(f"{i:<8} {d}")

# Giải thích từng đỉnh
print("\nGiải thích:")
print("Từ nguồn 0: dist = [0, 3, 1, 4, 7, 9]")
print("Từ nguồn 3: dist = [inf, inf, inf, 0, 3, 6]")
print("Kết hợp min: dist = [0, 3, 1, 0, 3, 6]")
