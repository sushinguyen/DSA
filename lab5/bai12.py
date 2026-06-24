"""
Bài 12. Đi qua đỉnh bắt buộc
Tìm đường đi ngắn nhất từ s tới t bắt buộc đi qua đỉnh k.
Công thức: dist(s→k) + dist(k→t)
Với đồ thị có hướng cần chạy Dijkstra trên đồ thị đảo để tính dist(k→t).
"""
import heapq

def dijkstra(n, adj, src):
    INF = float('inf')
    dist = [INF] * n
    dist[src] = 0
    heap = [(0, src)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))
    return dist


def shortest_path_through(n, adj, adj_rev, s, t, k):
    """
    Tìm đường đi ngắn nhất s→k→t.
    adj_rev: đồ thị đảo chiều (để tính dist từ t ngược lại)
    """
    dist_from_s = dijkstra(n, adj, s)       # dist(s → mọi đỉnh)
    dist_from_t = dijkstra(n, adj_rev, t)   # dist(t → mọi đỉnh) trên đồ thị đảo
                                             # = dist(mọi đỉnh → t) trên đồ thị gốc

    sk = dist_from_s[k]
    kt = dist_from_t[k]

    if sk == float('inf') or kt == float('inf'):
        return -1  # Không tồn tại đường đi

    return sk + kt


# --- Đồ thị G1 ---
adj_G1 = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5), (4, 8)],
    3: [(4, 3), (5, 6)],
    4: [(5, 2)],
    5: []
}

# Đồ thị đảo chiều
adj_G1_rev = {i: [] for i in range(6)}
for u, neighbors in adj_G1.items():
    for v, w in neighbors:
        adj_G1_rev[v].append((u, w))

n = 6
s, t, k = 0, 5, 2

result = shortest_path_through(n, adj_G1, adj_G1_rev, s, t, k)
print(f"Đường đi ngắn nhất từ {s} → {t} bắt buộc qua {k}: {result}")

# Phân tích chi tiết
dist_s = dijkstra(n, adj_G1, s)
dist_t = dijkstra(n, adj_G1_rev, t)
print(f"\ndist({s} → {k}) = {dist_s[k]}")
print(f"dist({k} → {t}) = {dist_t[k]}")
print(f"Tổng: {dist_s[k]} + {dist_t[k]} = {dist_s[k] + dist_t[k]}")

# Thử thêm ví dụ
print("\n--- Thêm ví dụ ---")
for mid in range(n):
    res = shortest_path_through(n, adj_G1, adj_G1_rev, s, t, mid)
    print(f"s=0 → k={mid} → t=5 : {res}")
