"""
Bài 16. Trọng số trên đỉnh (Node-weighted Dijkstra)
Chi phí nằm ở đỉnh thay vì cạnh.
Kỹ thuật: tách mỗi đỉnh v thành v_in và v_out, nối bằng cạnh có trọng số c[v].
Mọi cạnh gốc (u, v) → (u_out, v_in) với trọng số 0.
"""
import heapq

def node_weighted_dijkstra(n, edges, node_cost, src, dst):
    """
    n: số đỉnh gốc (0..n-1)
    edges: [(u, v), ...] cạnh vô hướng
    node_cost: [c0, c1, ..., cn-1]
    src, dst: nguồn và đích

    Biến đổi:
      Đỉnh v → v_in = 2v, v_out = 2v+1
      Cạnh nội bộ: v_in → v_out, trọng số = node_cost[v]
      Cạnh đồ thị: u_out → v_in (và v_out → u_in nếu vô hướng), trọng số = 0
    """
    N = 2 * n   # tổng số đỉnh sau biến đổi
    adj = [[] for _ in range(N)]

    # Cạnh nội bộ: v_in → v_out
    for v in range(n):
        v_in  = 2 * v
        v_out = 2 * v + 1
        adj[v_in].append((v_out, node_cost[v]))

    # Cạnh đồ thị (vô hướng): u_out → v_in và v_out → u_in
    for u, v in edges:
        u_out = 2*u + 1
        v_in  = 2*v
        v_out = 2*v + 1
        u_in  = 2*u
        adj[u_out].append((v_in, 0))
        adj[v_out].append((u_in, 0))   # bỏ dòng này nếu có hướng

    # Dijkstra trên đồ thị mở rộng
    INF = float('inf')
    dist = [INF] * N
    dist[2 * src] = 0   # bắt đầu tại src_in
    heap = [(0, 2 * src)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))

    # Chi phí tới dst là dist[dst_in] (bao gồm chi phí đỉnh src)
    result = dist[2 * dst]
    return result if result != INF else -1


# --- Ví dụ ---
# Đồ thị vô hướng: 0-1-2-3
# Chi phí đỉnh: [1, 2, 3, 1]
# Đường 0→1→2→3: chi phí = 1+2+3+1 = 7
# Đường 0→3 trực tiếp (nếu có): chi phí = 1+1 = 2
n = 4
edges = [(0,1), (1,2), (2,3), (0,3)]
node_cost = [1, 2, 3, 1]

print("Đồ thị vô hướng với trọng số trên đỉnh:")
print(f"node_cost = {node_cost}")
print(f"edges = {edges}\n")

for dst in range(n):
    cost = node_weighted_dijkstra(n, edges, node_cost, 0, dst)
    print(f"Chi phí ngắn nhất từ 0 → {dst}: {cost}")

print("\nGiải thích đường 0→3:")
print("  Qua 0→1→2→3: 1+2+3+1 = 7")
print("  Trực tiếp 0→3: 1+1 = 2  ← tối ưu")

# --- Kỹ thuật biến đổi ---
print("\n--- Kỹ thuật biến đổi đỉnh thành cạnh ---")
print("Mỗi đỉnh v được tách thành:")
print("  v_in  (= 2v)   : nơi nhận cạnh đến")
print("  v_out (= 2v+1) : nơi phát cạnh đi")
print("Cạnh nội bộ: v_in → v_out, w = node_cost[v]")
print("Cạnh đồ thị: u_out → v_in, w = 0")
