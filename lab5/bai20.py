"""
Bài 20. K Đường đi Ngắn nhất (K-Shortest Paths)
Tìm độ dài của K đường đi ngắn nhất từ s tới t (cho phép lặp đỉnh).
Thuật toán Yen / biến thể Dijkstra: một đỉnh được lấy ra tối đa K lần.
"""
import heapq

def k_shortest_paths(n, adj, src, dst, K):
    """
    Dijkstra mở rộng: đỉnh được lấy ra tối đa K lần.
    Lần thứ k được lấy ra → đó là đường thứ k ngắn nhất tới đỉnh đó.
    """
    # count[u] = số lần đỉnh u đã được lấy ra khỏi heap
    count = [0] * n
    results = []

    heap = [(0, src)]   # (cost, node)

    while heap and len(results) < K:
        d, u = heapq.heappop(heap)
        count[u] += 1

        if count[u] > K:
            continue

        if u == dst:
            results.append(d)

        for v, w in adj[u]:
            if count[v] < K:
                heapq.heappush(heap, (d + w, v))

    return results


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
K = 3
src, dst = 0, 4

results = k_shortest_paths(n, adj_G1, src, dst, K)

print(f"K={K} đường đi ngắn nhất từ {src} → {dst}:")
for i, cost in enumerate(results, 1):
    print(f"  Đường thứ {i}: {cost}")

print("\nGiải thích:")
print("  Đường 1: 0→2→1→3→4  = 1+2+1+3 = 7")
print("  Đường 2: 0→1→3→4    = 4+1+3   = 8")
print("  Đường 3: 0→2→3→4    = 1+5+3   = 9  (hoặc 0→2→4 = 1+8 = 9)")

# Demo với K lớn hơn
print(f"\n--- K=5 từ 0→5 ---")
results2 = k_shortest_paths(n, adj_G1, 0, 5, 5)
for i, cost in enumerate(results2, 1):
    print(f"  Đường thứ {i}: {cost}")

print("\n--- Nguyên lý thuật toán ---")
print("Dijkstra thường: mỗi đỉnh lấy ra 1 lần (lần đầu = ngắn nhất)")
print("K-shortest:      mỗi đỉnh lấy ra tối đa K lần")
print("  Lần 1 lấy ra  = đường ngắn nhất")
print("  Lần 2 lấy ra  = đường ngắn nhì")
print("  Lần k lấy ra  = đường ngắn thứ k")
print("Độ phức tạp: O(K(V+E)logV)")
