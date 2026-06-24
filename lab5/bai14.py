"""
Bài 14. Đường đi ngắn nhì (Second Shortest Path)
Tìm độ dài đường đi ngắn nhì từ s tới t (có thể dùng lại cạnh).
Gợi ý: lưu hai khoảng cách tốt nhất cho mỗi đỉnh.
"""
import heapq

def second_shortest(n, adj, src, dst):
    """
    dist1[u] = khoảng cách ngắn nhất tới u
    dist2[u] = khoảng cách ngắn nhì tới u
    Khi dist2[dst] được cập nhật lần đầu → đó là đáp án.
    """
    INF = float('inf')
    dist1 = [INF] * n
    dist2 = [INF] * n

    dist1[src] = 0
    heap = [(0, src)]  # (cost, node)

    while heap:
        d, u = heapq.heappop(heap)

        # Bỏ qua nếu đã có 2 đường tốt hơn
        if d > dist2[u]:
            continue

        for v, w in adj[u]:
            new_d = d + w
            if new_d < dist1[v]:
                dist2[v] = dist1[v]          # Đẩy cũ xuống vị trí 2
                dist1[v] = new_d
                heapq.heappush(heap, (dist1[v], v))
                heapq.heappush(heap, (dist2[v], v))
            elif dist1[v] < new_d < dist2[v]:
                dist2[v] = new_d             # Cập nhật đường ngắn nhì
                heapq.heappush(heap, (dist2[v], v))

    return dist1[dst], dist2[dst]


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
src, dst = 0, 4

shortest, second = second_shortest(n, adj_G1, src, dst)
print(f"Đường đi ngắn nhất  từ {src} → {dst}: {shortest}")
print(f"Đường đi ngắn nhì   từ {src} → {dst}: {second if second != float('inf') else 'Không tồn tại'}")

# Giải thích các đường từ 0→4:
print("\nCác đường từ 0 → 4 (G1):")
print("  0→2→1→3→4  = 1+2+1+3 = 7  ← ngắn nhất")
print("  0→1→3→4    = 4+1+3   = 8")
print("  0→2→3→4    = 1+5+3   = 9")
print("  0→2→4      = 1+8     = 9")
print(f"\n→ ngắn nhất = 7, ngắn nhì = 8")

# --- Ví dụ s=0, t=5 ---
src2, dst2 = 0, 5
sh2, sec2 = second_shortest(n, adj_G1, src2, dst2)
print(f"\nĐường đi ngắn nhất  từ {src2} → {dst2}: {sh2}")
print(f"Đường đi ngắn nhì   từ {src2} → {dst2}: {sec2 if sec2 != float('inf') else 'Không tồn tại'}")
