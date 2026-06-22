import heapq

def dijkstra_early_stop(adj, s, t):
    n = len(adj)
    dist = [float('inf')] * n
    dist[s] = 0
    heap = [(0, s)] 

    while heap:
        d, u = heapq.heappop(heap)

        if d > dist[u]: 
            continue

        if u == t:   
            return dist[t]

        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))

    return dist[t] if dist[t] != float('inf') else -1


# Đồ thị G1
adj = [
    [(1,4),(2,1)],  
    [(3,1)],      
    [(1,2),(3,5),(4,8)], 
    [(4,3),(5,6)],   
    [(5,2)],        
    []             
]

print(dijkstra_early_stop(adj, 0, 4))  