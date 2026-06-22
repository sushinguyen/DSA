import heapq
import time
import random

def dijkstra_v2(adj_list, s, n):
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

        for v, w in adj_list[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    return dist

def dijkstra_heap(adj_list, s, n):
    dist = [float('inf')] * n
    dist[s] = 0
    heap = [(0, s)]  

    while heap:
        d, u = heapq.heappop(heap)     

        if d > dist[u]:                
            continue

        for v, w in adj_list[u]:
            new_d = d + w
            if new_d < dist[v]:
                dist[v] = new_d
                heapq.heappush(heap, (new_d, v))   

    return dist

print("=" * 50)
print("TEST VỚI ĐỒ THỊ G1 (6 đỉnh, nguồn s=0)")
print("=" * 50)

adj_g1 = [
    [(1, 4), (2, 1)],          
    [(3, 1)],                   
    [(1, 2), (3, 5), (4, 8)],  
    [(4, 3), (5, 6)],            
    [(5, 2)],                    
    []                           
]
n_g1 = 6

res_v2   = dijkstra_v2(adj_g1, 0, n_g1)
res_heap = dijkstra_heap(adj_g1, 0, n_g1)

print(f"O(V²)   dist: {res_v2}")
print(f"O(ElogV) dist: {res_heap}")
print(f"Kết quả giống nhau: {res_v2 == res_heap}")


print()
print("=" * 50)
print("BENCHMARK – đồ thị thưa ngẫu nhiên")
print("=" * 50)

def gen_sparse_graph(n, m):
    """Sinh đồ thị có hướng ngẫu nhiên n đỉnh, m cạnh, trọng số 1–100."""
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = random.randint(0, n - 1)
        v = random.randint(0, n - 1)
        w = random.randint(1, 100)
        adj[u].append((v, w))
    return adj

configs = [
    (500,   1_000),
    (2_000, 4_000),
    (5_000, 10_000),
]

for n, m in configs:
    adj = gen_sparse_graph(n, m)

    t0 = time.perf_counter()
    dijkstra_v2(adj, 0, n)
    t_v2 = time.perf_counter() - t0

    t0 = time.perf_counter()
    dijkstra_heap(adj, 0, n)
    t_heap = time.perf_counter() - t0

    speedup = t_v2 / t_heap if t_heap > 0 else float('inf')
    print(f"n={n:>5}, m={m:>6} | O(V²): {t_v2*1000:7.2f}ms | Heap: {t_heap*1000:7.2f}ms | nhanh hơn x{speedup:.1f}")



print()
print("=" * 50)
print("PHÂN TÍCH ĐỘ PHỨC TẠP")
print("=" * 50)
print("""
Bản O(V²):
  Vòng ngoài  : V  lần
  Tìm min     : O(V) mỗi lần
  Relax cạnh  : O(E) tổng cộng
  → Tổng      : O(V²)

Bản Heap O((V+E)logV):
  Mỗi đỉnh push/pop heap : O(V log V)
  Mỗi cạnh relax + push  : O(E log V)
  → Tổng                 : O((V+E) log V)

Khi nào dùng cái nào?
  E ≈ V²  (đồ thị DÀY) → O(V²)     tốt hơn  
  E ≈ V   (đồ thị THƯA) → Heap      tốt hơn 
  Thực tế competitive  → Luôn dùng Heap cho an toàn
""")