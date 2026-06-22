import math
def dijkstra (graph, start ):
    n = len (graph)
    dist = {node: math.inf for node in graph}
    dist[start] = 0
    visited = {node: False for node in graph}
    for _ in range (n):
        u = None
        min_dist = math.inf
        for node in graph:
            if not visited[node] and dist[node] < min_dist:
                min_dist = dist[node]
                u = node
        if u is None:
            break
        visited[u] = True

        for v, weight in graph[u]:
            if not visited[v] and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
    return dist

adj = {
    'A': [('B', 5), ('C', 3)],
    'B': [('A', 5), ('C', 1), ('D', 2)],
    'C': [('A', 3), ('B', 1), ('D', 6)],
    'D': [('B', 2), ('C', 6), ('E', 4)],
    'E': [('D', 4)]
}

start_node = 'A'
distances = dijkstra(adj, start_node)
print(f"Khoảng cách ngắn nhất từ nguồn {start_node}:")
for node, distance in distances.items():
    print(f"Thành phố {node}: {distance}")