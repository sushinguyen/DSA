"""
Bài 15. Dijkstra trên lưới (Grid)
Chi phí khi bước vào mỗi ô (cell cost).
Tìm tổng chi phí nhỏ nhất từ ô trên-trái (0,0) tới ô dưới-phải (R-1, C-1).
Di chuyển 4 hướng: trên, dưới, trái, phải.
"""
import heapq

def dijkstra_grid(grid):
    """
    grid[r][c] = chi phí khi bước VÀO ô (r, c)
    Chi phí bắt đầu = grid[0][0] (chi phí ô xuất phát)
    """
    R, C = len(grid), len(grid[0])
    INF = float('inf')
    dist = [[INF] * C for _ in range(R)]
    dist[0][0] = grid[0][0]

    heap = [(grid[0][0], 0, 0)]   # (cost, row, col)
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]

    while heap:
        d, r, c = heapq.heappop(heap)
        if d > dist[r][c]:
            continue
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C:
                new_d = dist[r][c] + grid[nr][nc]
                if new_d < dist[nr][nc]:
                    dist[nr][nc] = new_d
                    heapq.heappush(heap, (new_d, nr, nc))

    return dist[R-1][C-1], dist


def reconstruct_path(grid, dist):
    """Truy vết đường đi từ đích ngược về nguồn."""
    R, C = len(grid), len(grid[0])
    path = []
    r, c = R-1, C-1
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    while (r, c) != (0, 0):
        path.append((r, c))
        for dr, dc in dirs:
            pr, pc = r + dr, c + dc
            if 0 <= pr < R and 0 <= pc < C:
                if dist[pr][pc] + grid[r][c] == dist[r][c]:
                    r, c = pr, pc
                    break
    path.append((0, 0))
    return list(reversed(path))


# --- Lưới 3×3 từ bài ---
grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]

total_cost, dist_grid = dijkstra_grid(grid)

print("Lưới chi phí:")
for row in grid:
    print("  ", row)

print(f"\nChi phí nhỏ nhất từ (0,0) → (2,2): {total_cost}")

print("\nBảng dist[][]:")
for row in dist_grid:
    print("  ", [x if x != float('inf') else '∞' for x in row])

path = reconstruct_path(grid, dist_grid)
print(f"\nĐường đi: {' → '.join(str(p) for p in path)}")
total = sum(grid[r][c] for r, c in path)
print(f"Tổng chi phí xác nhận: {total}")

# So sánh các đường có thể
print("\nCác đường từ (0,0)→(2,2):")
print("  (0,0)→(0,1)→(0,2)→(1,2)→(2,2): 1+3+1+1+1 = 7")
print("  (0,0)→(1,0)→(2,0)→(2,1)→(2,2): 1+1+4+2+1 = 9")
print("  (0,0)→(0,1)→(1,1)→(2,1)→(2,2): 1+3+5+2+1 = 12")
print("→ Đường ngắn nhất = 7")
