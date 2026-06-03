def find_kth_positive(a, k):
    left, right = 0, len(a) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        missing_count = a[mid] - (mid + 1)
        
        if missing_count < k:
            left = mid + 1
        else:
            right = mid - 1
            
    return left + k

a = [2, 3, 4, 7, 11]
k = int(input("Nhập: "))
result = find_kth_positive(a, k)

print(f"Số nguyên dương thứ {k} bị thiếu là: {result}")