"""
Bài 22. Giới hạn số cạnh trung chuyển
Tìm đường đi rẻ nhất từ s tới t dùng tối đa k cạnh (k điểm dừng = k+1 cạnh).
Trạng thái: (đỉnh, số_cạnh_đã_dùng)
"""
import heapq
from math import inf

def dijkstra_max_edges(n, adj, src, dst, max_edges):
    """
    Tìm đường đi rẻ nhất từ src → dst dùng tối đa max_edges cạnh.
    Trạng thái: (chi_phí, đỉnh, số_cạnh_đã_dùng)
    dist[u][e] = chi phí nhỏ nhất tới u dùng đúng e cạnh
    """
    INF = float('inf')
    # dist[node][edges_used] = min cost
    dist = [[INF] * (max_edges + 1) for _ in range(n)]
    dist[src][0] = 0

    heap = [(0, src, 0)]  # (cost, node, edges_used)

    while heap:
        cost, u, edges = heapq.heappop(heap)
        if cost > dist[u][edges]:
            continue
        if edges >= max_edges:
            continue   # Không được dùng thêm cạnh
        for v, w in adj[u]:
            new_cost  = cost + w
            new_edges = edges + 1
            if new_cost < dist[v][new_edges]:
                dist[v][new_edges] = new_cost
                heapq.heappush(heap, (new_cost, v, new_edges))

    # Lấy min trên tất cả số cạnh ≤ max_edges
    best = min(dist[dst])
    return best if best != INF else -1


def dijkstra_max_edges_with_path(n, adj, src, dst, max_edges):
    """Kèm truy vết đường đi."""
    INF = float('inf')
    dist   = [[INF] * (max_edges + 1) for _ in range(n)]
    parent = [[(-1, -1)] * (max_edges + 1) for _ in range(n)]  # (prev_node, prev_edges)
    dist[src][0] = 0

    heap = [(0, src, 0)]

    while heap:
        cost, u, edges = heapq.heappop(heap)
        if cost > dist[u][edges]:
            continue
        if edges >= max_edges:
            continue
        for v, w in adj[u]:
            new_cost  = cost + w
            new_edges = edges + 1
            if new_cost < dist[v][new_edges]:
                dist[v][new_edges]   = new_cost
                parent[v][new_edges] = (u, edges)
                heapq.heappush(heap, (new_cost, v, new_edges))

    # Tìm số cạnh tốt nhất
    best_e = min(range(max_edges + 1), key=lambda e: dist[dst][e])
    if dist[dst][best_e] == INF:
        return -1, []

    # Reconstruct
    path = []
    cur, e = dst, best_e
    while cur != -1:
        path.append(cur)
        prev_node, prev_e = parent[cur][e]
        cur, e = prev_node, prev_e
    path.reverse()
    return dist[dst][best_e], path


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
dst = 5

print("Chi phí ngắn nhất từ 0 → 5 với giới hạn số cạnh:")
print(f"{'Max cạnh':<10} {'Chi phí':<10} {'Đường đi'}")
print("-" * 45)
for k in range(1, 7):
    cost, path = dijkstra_max_edges_with_path(n, adj_G1, 0, dst, k)
    path_str = ' → '.join(map(str, path)) if path else 'Không tồn tại'
    print(f"{k:<10} {str(cost):<10} {path_str}")

print("\nGiải thích:")
print("  Với k=1: không thể tới đỉnh 5 chỉ qua 1 cạnh → -1")
print("  Với k=3: 0→2→3→5 = 1+5+6 = 12 (3 cạnh)")
print("  Với k=4: 0→2→1→3→5 = 1+2+1+6 = 10 (4 cạnh)")
print("  Với k=5: 0→2→1→3→4→5 = 1+2+1+3+2 = 9 (5 cạnh) ← tối ưu tổng thể")
