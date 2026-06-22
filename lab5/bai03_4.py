import math
def dijkstra (graph, start ):
    n = len (graph)
    dist = [math.inf] * n
    dist [start] = 0
    visited = [False] * n
    for _ in range (n):
        u = -1
        min_dist = math.inf
        for i in range (n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i
        if u == -1:
            break
        visited[u] = True

        for v, weight in graph[u]:
            if not visited[v] and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight

    return dist
    
adj = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5), (4, 8)],
    3: [(5, 6), (4, 3)],
    4: [(5, 2)],
    5: []
}

start_node = 0
distances = dijkstra(adj, start_node)
print(f"Khoảng cách ngắn nhất từ nguồn s={start_node} đến các đỉnh:")
for i in range(len(distances)):
    if distances[i] == math.inf:
            print(f"Đỉnh {i}: -1 (Không thể tới)")
    else:
        print(f"Đỉnh {i}: {distances[i]}")