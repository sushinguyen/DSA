import math
import sys

class Graph():
    def __init__(cung, dinh):
        cung.x = dinh
        cung.graph = [[0 for column in range(dinh)] for row in range(dinh)]
        
    def inketqua(cung, L, a):
        # Mảng ánh xạ ngược từ số sang tên chữ cái của đỉnh để in ra trực quan
        ten_dinh = ['a', 'b', 'c', 'd', 'e', 'z']
        print("đỉnh nguồn xuất phát từ: ", ten_dinh[a])
        for nut in range(cung.x):
            do_dai = L[nut] if L[nut] != sys.maxsize else "Không có đường đi"
            print(ten_dinh[a], " đến đỉnh ", ten_dinh[nut], "độ dài đường đi là: ", do_dai)
            
    def duongdinhonhat(cung, L, P):
        min = sys.maxsize
        min_index = -1
        for x in range(cung.x):
            if L[x] < min and P[x] == False:
                min = L[x]
                min_index = x
        return min_index
        
    def timduongdi(cung, a):
        L = [sys.maxsize] * cung.x
        L[a] = 0
        P = [False] * cung.x
        
        for cout in range(cung.x):
            u = cung.duongdinhonhat(L, P)
            if u == -1: 
                break
            P[u] = True
            for x in range(cung.x):
                if cung.graph[u][x] > 0 and P[x] == False and L[x] > L[u] + cung.graph[u][x]:
                    L[x] = L[u] + cung.graph[u][x]
                    
        cung.inketqua(L, a)

# Khởi tạo đồ thị có hướng với 6 đỉnh: a(0), b(1), c(2), d(3), e(4), z(5)
g4 = Graph(6)
g4.graph = [
    [0, 2, 0, 5, 0, 0],  # Từ a -> b(2), d(5)
    [0, 0, 7, 0, 1, 0],  # Từ b -> c(7), e(1)
    [0, 0, 0, 0, 0, 1],  # Từ c -> z(1)
    [0, 0, 0, 0, 6, 0],  # Từ d -> e(6)
    [0, 0, 3, 0, 0, 2],  # Từ e -> c(3), z(2)
    [0, 0, 0, 0, 0, 0]   # Từ z không có đường đi ra
]

# Tìm đường đi ngắn nhất bắt đầu từ đỉnh 'a' (chỉ số 0) đến đỉnh 'z'
g4.timduongdi(0)