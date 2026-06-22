import heapq
import time
import random

# ============================================================
# 2 BẢN DIJKSTRA
# ============================================================
def dijkstra_v2(adj, s, n):
    dist = [float('inf')] * n
    visited = [False] * n
    dist[s] = 0
    for _ in range(n):
        u = -1
        for i in range(n):
            if not visited[i] and (u == -1 or dist[i] < dist[u]):
                u = i
        if u == -1 or dist[u] == float('inf'):
            break
        visited[u] = True
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    return dist

def dijkstra_heap(adj, s, n):
    dist = [float('inf')] * n
    dist[s] = 0
    heap = [(0, s)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(heap, (nd, v))
    return dist

def gen_graph(n, density):
    """
    density = 'sparse' → E ≈ V   (đồ thị thưa)
    density = 'medium' → E ≈ V*logV
    density = 'dense'  → E ≈ V²  (đồ thị dày)
    """
    adj = [[] for _ in range(n)]
    if density == 'sparse':
        m = n                      
    elif density == 'medium':
        m = n * 10                 
    else:                   
        m = n * n // 4            
    edges_added = 0
    for u in range(n):
        for v in range(n):
            if u != v and edges_added < m:
                w = random.randint(1, 100)
                adj[u].append((v, w))
                edges_added += 1
    return adj, edges_added


def print_theory():
    print("=" * 60)
    print("PHÂN TÍCH ĐỘ PHỨC TẠP")
    print("=" * 60)
    print("""
┌─────────────┬──────────────────┬──────────────────────────┐
│             │   Bản O(V²)      │   Bản Heap O((V+E)logV)  │
├─────────────┼──────────────────┼──────────────────────────┤
│ Tìm min     │ Duyệt dist[] O(V)│ heappop()  O(log V)      │
│ Cập nhật    │ Gán trực tiếp    │ heappush() O(log V)      │
│ Tổng        │ O(V²)            │ O((V+E) log V)           │
└─────────────┴──────────────────┴──────────────────────────┘

Khi E ≈ V² (đồ thị DÀY):
  Heap → O((V + V²) log V) = O(V² log V)   ← CHẬM HƠN
  V²   → O(V²)                              ← TỐT HƠN 

Khi E ≈ V (đồ thị THƯA)
  Heap → O((V + V) log V)  = O(V log V)    ← TỐT HƠN 
  V²   → O(V²)                              ← CHẬM HƠN

Điểm hòa vốn (break-even):
  O(V²) = O((V+E) log V)
  → E ≈ V² / log V

  Nếu E >> V²/logV → dùng O(V²)
  Nếu E << V²/logV → dùng Heap
""")

print_theory()

print("=" * 60)
print("BENCHMARK THỰC TẾ (n = 300)")
print("=" * 60)

n = 300
random.seed(42)

for density in ['sparse', 'medium', 'dense']:
    adj, m = gen_graph(n, density)

    t0 = time.perf_counter()
    for _ in range(5):           # lặp 5 lần để ổn định
        dijkstra_v2(adj, 0, n)
    t_v2 = (time.perf_counter() - t0) / 5

    t0 = time.perf_counter()
    for _ in range(5):
        dijkstra_heap(adj, 0, n)
    t_heap = (time.perf_counter() - t0) / 5

    ratio = m / (n * n)
    winner = "O(V²) ✅" if t_v2 < t_heap else "Heap ✅"
    print(f"\nMật độ: {density:6s} | V={n}, E={m:>6} | E/V²={ratio:.3f}")
    print(f"  O(V²) : {t_v2*1000:7.3f} ms")
    print(f"  Heap  : {t_heap*1000:7.3f} ms")
    print(f"  → Nên dùng: {winner}")

print()
print("=" * 60)
print("BẢNG QUYẾT ĐỊNH THỰC TẾ")
print("=" * 60)
print("""
  E / V²  │ Loại đồ thị │ Nên dùng
──────────┼─────────────┼──────────────────────────
  > 0.5   │ Dày         │ O(V²)  – mảng đơn giản
  0.1–0.5 │ Trung bình  │ Heap   – an toàn hơn
  < 0.1   │ Thưa        │ Heap   – nhanh hơn rõ
──────────┼─────────────┼──────────────────────────

Gợi nhớ nhanh:
  • Bản đồ thành phố (đường phố)    → Thưa  → Heap
  • Mạng xã hội (mọi người kết bạn) → Dày   → O(V²)
  • Competitive programming          → Heap  (luôn an toàn)
  • V ≤ 1000, bất kỳ E              → O(V²) (đủ nhanh)
  • V > 10^4                        → Heap  (bắt buộc)
""")