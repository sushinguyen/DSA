def find_Median_Sorted_Arrays(a, b):
    if len(a) > len(b):
        a, b = b, a
        
    m, n = len(a), len(b)
    low, high = 0, m
    
    while low <= high:
        i = (low + high) // 2
        j = (m + n + 1) // 2 - i
        
        A_left = a[i - 1] if i > 0 else float('-inf')
        A_right = a[i] if i < m else float('inf')
        
        B_left = b[j - 1] if j > 0 else float('-inf')
        B_right = b[j] if j < n else float('inf')
        
        if A_left <= B_right and B_left <= A_right:
            if (m + n) % 2 == 1:
                return float(max(A_left, B_left))
            else:
                return (max(A_left, B_left) + min(A_right, B_right)) / 2.0
                
        elif A_left > B_right:
            high = i - 1
        else:
            low = i + 1
            
    return 0.0

print(find_Median_Sorted_Arrays([1, 3], [2]))

print(find_Median_Sorted_Arrays([1, 2], [3, 4]))