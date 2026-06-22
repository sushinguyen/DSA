def dijkstra(graph, start):
    n = len(graph)          
Đếm số đỉnh trong đồ thị (ở đây n = 6, vì có đỉnh 0→5)

    dist = [math.inf] * n  
    Tạo mảng khoảng cách, ban đầu tất cả = vô cực (chưa biết đường đi)

    dist [start] = 0
    Khoảng cách từ đỉnh nguồn đến chính nó = 0

    visited = [False] * n
    Mảng đánh dấu: đỉnh nào đã được xử lý xong chưa

    for _ in range (n):
    Lặp tối đa n lần (mỗi lần chọn 1 đỉnh chưa thăm có dist nhỏ nhất)

        u = -1
        min_dist = math.inf
        for i in range (n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i
        Tìm đỉnh u chưa thăm có khoảng cách nhỏ nhất hiện tại
       ( thay thế cho priority queue để đơn giản)

        if u == -1:
            break
        Nếu không tìm được đỉnh nào → tất cả đã thăm hoặc không còn đỉnh nào 
        
        visited[u] = True
        đánh dấu các đỉnh đã xử lý xong

        for v, weight in graph[u]:
        Duyệt tất cả đỉnh kề v của u, weight là trọng số cạnh (u → v)

            if not visited[v] and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
            Nếu v chưa thăm VÀ đi qua u thì ngắn hơn → cập nhật dist[v]
            (đây là bước "relax" cạnh)   
    return dist
    Trả về mảng khoảng cách ngắn nhất từ start đến tất cả các đỉnh
