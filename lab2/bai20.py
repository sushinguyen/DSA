def is_valid(p, m, max_pages_allowed):
    student_count = 1
    current_pages_sum = 0
    
    for pages in p:
        if pages > max_pages_allowed:
            return False
            
        if current_pages_sum + pages > max_pages_allowed:
            student_count += 1
            current_pages_sum = pages
            
            if student_count > m:
                return False
        else:
            current_pages_sum += pages
            
    return True

def allocate_books(p, m):
    if len(p) < m:
        return -1 
        
    low = max(p)
    high = sum(p)
    result = high
    
    while low <= high:
        mid = (low + high) // 2
        
        if is_valid(p, m, mid):
            result = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return result

p = [12, 34, 67, 90]
m = 2
print(f"Số trang tối đa của một học sinh nhỏ nhất là: {allocate_books(p, m)}")