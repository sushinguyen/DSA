def search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    m = len(matrix)     
    n = len(matrix[0]) 
    low = 0
    high = m * n - 1
    
    while low <= high:
        mid = (low + high) // 2
        mid_val = matrix[mid // n][mid % n]
        
        if mid_val == target:
            return True
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

matrix = [[1, 3, 5], [7, 9, 11]]
x = 9
print(f"Tìm thấy {x} trong ma trận: {search_matrix(matrix, x)}")