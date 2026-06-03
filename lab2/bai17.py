def ship_within_days(w, D):
    left = max(w)
    right = sum(w)
    
    def can_ship(capacity):
        days_needed = 1
        current_weight = 0
        
        for weight in w:
            if current_weight + weight > capacity:
                days_needed += 1
                current_weight = weight
            else:
                current_weight += weight
                
        return days_needed <= D

    while left < right:
        mid = (left + right) // 2
        
        if can_ship(mid):
            right = mid
        else:
            left = mid + 1
            
    return left

w = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
D = int(input("Nhập: "))
result = ship_within_days(w, D)

print(f"Sức chứa nhỏ nhất của tàu hàng là: {result}")