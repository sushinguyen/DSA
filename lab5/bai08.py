import heapq

def dijkstra(adj, s):
    n = len(adj)
    dist = [float('inf')] * n
    dist[s] = 0
    heap = [(0, s)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))

    return dist

def count_in_radius(adj, s, D):
    dist = dijkstra(adj, s)

    in_radius = [i for i, d in enumerate(dist) if d <= D]

    print(f"D = {D}") 
    print(f"Số đỉnh: {len(in_radius)}")
    print(f"Các đỉnh: {in_radius}")
    return len(in_radius)

adj = [
    [(1,4),(2,1)],
    [(3,1)],
    [(1,2),(3,5),(4,8)],
    [(4,3),(5,6)],
    [(5,2)],
    []
]

count_in_radius(adj, 0, 3)   
print()
count_in_radius(adj, 0, 7)   