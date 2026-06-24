"""
Bài 21. Dijkstra trên Trạng thái Mở rộng
Trạng thái = (đỉnh, thông tin phụ)
Ví dụ: (đỉnh, nhiên_liệu_còn_lại) — xe có bình nhiên liệu tối đa F.
Mỗi cạnh tiêu thụ fuel(u,v) nhiên liệu.
Có thể nạp nhiên liệu tại một số trạm.
"""
import heapq

def dijkstra_with_fuel(n, adj, refuel_stations, src, dst, max_fuel, start_fuel=None):
    """
    adj[u] = [(v, cost, fuel_needed), ...]
    refuel_stations: set các đỉnh có trạm xăng
    max_fuel: dung tích bình nhiên liệu tối đa
    
    Trạng thái: (chi_phí, đỉnh, nhiên_liệu_còn)
    dist[u][f] = chi phí nhỏ nhất tới đỉnh u với f nhiên liệu còn lại
    """
    if start_fuel is None:
        start_fuel = max_fuel

    INF = float('inf')
    # dist[node][fuel] = min cost
    dist = [[INF] * (max_fuel + 1) for _ in range(n)]
    dist[src][start_fuel] = 0

    heap = [(0, src, start_fuel)]  # (cost, node, fuel)

    while heap:
        cost, u, fuel = heapq.heappop(heap)
        if cost > dist[u][fuel]:
            continue
        if u == dst:
            return cost

        # Nạp nhiên liệu tại trạm
        if u in refuel_stations and fuel < max_fuel:
            full = max_fuel
            if dist[u][full] > cost:
                dist[u][full] = cost
                heapq.heappush(heap, (cost, u, full))

        # Di chuyển qua các cạnh
        for v, edge_cost, fuel_needed in adj[u]:
            if fuel >= fuel_needed:
                new_fuel = fuel - fuel_needed
                new_cost = cost + edge_cost
                if new_cost < dist[v][new_fuel]:
                    dist[v][new_fuel] = new_cost
                    heapq.heappush(heap, (new_cost, v, new_fuel))

    return -1  # Không thể tới đích


# --- Ví dụ 1: Đường đi đơn giản với nhiên liệu ---
# Đồ thị: 0→1→2→3→4
# Mỗi cạnh tốn 1 nhiên liệu, chi phí = trọng số cạnh
# Bình nhiên liệu tối đa = 2, trạm xăng tại đỉnh 2
adj1 = {
    0: [(1, 1, 1)],   # (tới đỉnh 1, chi phí 1, tốn 1 nhiên liệu)
    1: [(2, 2, 1)],
    2: [(3, 1, 1)],
    3: [(4, 3, 1)],
    4: []
}
refuel = {2}   # trạm xăng tại đỉnh 2
max_fuel = 2

result = dijkstra_with_fuel(5, adj1, refuel, 0, 4, max_fuel)
print(f"Chi phí từ 0→4 (bình xăng tối đa {max_fuel}, trạm xăng tại 2): {result}")

# --- Ví dụ 2: Không có trạm xăng → không đủ nhiên liệu ---
result2 = dijkstra_with_fuel(5, adj1, set(), 0, 4, max_fuel)
print(f"Chi phí từ 0→4 (không có trạm xăng): {result2}")

# --- Ví dụ 3: Đặt vé miễn phí (biến thể) ---
print("\n--- Biến thể: Vé miễn phí (free edges) ---")
print("""
Trạng thái = (đỉnh, số_vé_miễn_phí_còn_lại)
Ý nghĩa: được dùng tối đa K cạnh với chi phí 0.

def dijkstra_free_tickets(n, adj, src, dst, K):
    dist = [[INF]*(K+1) for _ in range(n)]
    dist[src][K] = 0
    heap = [(0, src, K)]
    while heap:
        cost, u, tickets = heappop(heap)
        if cost > dist[u][tickets]: continue
        if u == dst: return cost
        for v, w in adj[u]:
            # Đi bình thường
            if cost + w < dist[v][tickets]:
                dist[v][tickets] = cost + w
                heappush(heap, (cost + w, v, tickets))
            # Dùng vé miễn phí
            if tickets > 0 and cost < dist[v][tickets-1]:
                dist[v][tickets-1] = cost
                heappush(heap, (cost, v, tickets-1))
    return dist[dst][0] if dist[dst][0] != INF else -1
""")

print("Độ phức tạp: O((V × F + E) log(V × F))")
print("với F = dung tích bình nhiên liệu (hoặc số vé)")
