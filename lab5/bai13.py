"""
Bài 13. Đếm số đường đi ngắn nhất
Đếm số lượng đường đi ngắn nhất khác nhau từ nguồn tới mỗi đỉnh.
"""
import heapq

def count_shortest_paths(n, adj, src):
    """
    Trả về:
      dist[i]  = độ dài đường đi ngắn nhất từ src tới i
      count[i] = số đường đi ngắn nhất tới i
    """
    INF = float('inf')
    dist  = [INF] * n
    count = [0]   * n

    dist[src]  = 0
    count[src] = 1
    heap = [(0, src)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            new_d = dist[u] + w
            if new_d < dist[v]:
                dist[v]  = new_d
                count[v] = count[u]          # Đường mới ngắn hơn → reset count
                heapq.heappush(heap, (new_d, v))
            elif new_d == dist[v]:
                count[v] += count[u]         # Bằng nhau → cộng thêm số đường

    return dist, count


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
dist, count = count_shortest_paths(n, adj_G1, 0)

print("Đếm số đường đi ngắn nhất từ nguồn 0:")
print(f"{'Đỉnh':<6} {'dist':<8} {'Số đường đi ngắn nhất'}")
print("-" * 35)
for i in range(n):
    d = dist[i] if dist[i] != float('inf') else '∞'
    print(f"{i:<6} {str(d):<8} {count[i]}")

# --- Đồ thị có nhiều đường bằng nhau để demo ---
print("\n--- Demo đồ thị có nhiều đường ngắn nhất bằng nhau ---")
# 0→1 (w=2), 0→2 (w=1), 2→1 (w=1), 1→3 (w=5), 2→3 (w=6)
# dist[1] = 2 qua (0→1) hoặc (0→2→1) → 2 đường
adj2 = {
    0: [(1, 2), (2, 1)],
    1: [(3, 5)],
    2: [(1, 1), (3, 6)],
    3: []
}
dist2, count2 = count_shortest_paths(4, adj2, 0)
print(f"{'Đỉnh':<6} {'dist':<8} {'Số đường đi ngắn nhất'}")
print("-" * 35)
for i in range(4):
    d = dist2[i] if dist2[i] != float('inf') else '∞'
    print(f"{i:<6} {str(d):<8} {count2[i]}")
