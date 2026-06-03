def kthSmallest_binary_search(matrix, k):
    n = len(matrix)
    
    def countLessOrEqual(target):
        count = 0
        r = n - 1
        c = 0
        
        while r >= 0 and c < n:
            if matrix[r][c] <= target:
                count += (r + 1)
                c += 1
            else:
                r -= 1
        return count

    low = matrix[0][0]
    high = matrix[n-1][n-1]
    
    while low < high:
        mid = (low + high) // 2
        if countLessOrEqual(mid) >= k:
            high = mid
        else:
            low = mid + 1
            
    return low

matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
k = 8
print(f"Kết quả (Binary Search): {kthSmallest_binary_search(matrix, k)}")