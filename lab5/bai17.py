"""
Bài 17. Đường đi Bottleneck (Minimax)
Tìm đường đi từ s tới t sao cho cạnh lớn nhất trên đường là nhỏ nhất.
Biến đổi phép relax: thay vì tổng → lấy max.
"""
import heapq

def minimax_dijkstra(n, adj, src, dst):
    """
    dist[u] = giá trị cạnh lớn nhất nhỏ nhất trên đường từ src tới u.
    Phép relax: dist[v] = min(dist[v], max(dist[u], w(u,v)))
    """
    INF = float('inf')
    dist = [INF] * n
    dist[src] = 0
    heap = [(0, src)]   # (bottleneck hiện tại, đỉnh)

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        if u == dst:
            return dist[dst]
        for v, w in adj[u]:
            new_d = max(dist[u], w)     # ← Đây là sự khác biệt so với Dijkstra thông thường
            if new_d < dist[v]:
                dist[v] = new_d
                heapq.heappush(heap, (new_d, v))

    return dist[dst] if dist[dst] != INF else -1


def minimax_with_path(n, adj, src, dst):
    """Minimax kèm truy vết đường đi."""
    INF = float('inf')
    dist   = [INF] * n
    parent = [-1]  * n
    dist[src] = 0
    heap = [(0, src)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            new_d = max(dist[u], w)
            if new_d < dist[v]:
                dist[v]   = new_d
                parent[v] = u
                heapq.heappush(heap, (new_d, v))

    # Reconstruct path
    path = []
    cur = dst
    while cur != -1:
        path.append(cur)
        cur = parent[cur]
    path.reverse()

    return dist[dst] if dist[dst] != INF else -1, path


# --- Đồ thị G1 ---
adj_G1 = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5), (4, 8)],
    3: [(4, 3), (5, 6)],
    4: [(5, 2)],
    5: []
}

n = 6
print("Minimax (Bottleneck) Dijkstra trên G1:")
print(f"{'s→t':<8} {'Bottleneck':<12} {'Đường đi'}")
print("-" * 45)

for dst in range(1, 6):
    result, path = minimax_with_path(n, adj_G1, 0, dst)
    print(f"0→{dst}     {result:<12} {' → '.join(map(str, path))}")

print("\nGiải thích (0→5):")
print("  Đường 0→2→1→3→5: max(1,2,1,6) = 6")
print("  Đường 0→1→3→5:   max(4,1,6)   = 6")
print("  Đường 0→2→3→5:   max(1,5,6)   = 6")
print("  Đường 0→2→1→3→4→5: max(1,2,1,3,2) = 3  ← nhỏ nhất!")

print("\n--- So sánh phép relax ---")
print("Dijkstra thường  : dist[v] = min(dist[v], dist[u] + w)")
print("Minimax Dijkstra : dist[v] = min(dist[v], max(dist[u], w))")
