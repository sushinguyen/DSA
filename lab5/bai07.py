import heapq

def dijkstra_path(adj, s, t):
    n = len(adj)
    dist = [float('inf')] * n
    parent = [-1] * n
    dist[s] = 0
    heap = [(0, s)]

    while heap:
        d, u = heapq.heappop(heap)

        if d > dist[u]:
            continue

        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u          
                heapq.heappush(heap, (dist[v], v))


    path = []
    node = t
    while node != -1:
        path.append(node)
        node = parent[node]
    path.reverse()

    if path[0] != s:
        return -1, []

    return dist[t], path

adj = [
    [(1,4),(2,1)],
    [(3,1)],
    [(1,2),(3,5),(4,8)],
    [(4,3),(5,6)],
    [(5,2)],
    []
]

cost, path = dijkstra_path(adj, 0, 4)
print(f"Độ dài: {cost}")          
print(f"Đường đi: {' → '.join(map(str, path))}") 