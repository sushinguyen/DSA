def can_split(a, k, max_sum_allowed):
    segment_count = 1
    current_sum = 0
    
    for num in a:
        if num > max_sum_allowed:
            return False
            
        if current_sum + num > max_sum_allowed:
            segment_count += 1
            current_sum = num
            
            if segment_count > k:
                return False
        else:
            current_sum += num
            
    return True

def split_array_largest_sum(a, k):
    if len(a) < k:
        return -1
        
    low = max(a)
    high = sum(a)
    result = high
    
    while low <= high:
        mid = (low + high) // 2
        
        if can_split(a, k, mid):
            result = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return result

a = [7, 2, 5, 10, 8]
k = 2
print(f"Tổng lớn nhất trong các đoạn sau khi chia là nhỏ nhất: {split_array_largest_sum(a, k)}")