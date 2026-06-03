def minimize_Max_Distance(x, k):
    distances = [x[i+1] - x[i] for i in range(len(x) - 1)]
    
    def isValid(mid):
        stations_needed = 0
        for dist in distances:
            stations_needed += int(dist / mid)
        return stations_needed <= k

    low = 0.0
    high = max(distances)
    
    for _ in range(80):
        mid = (low + high) / 2.0
        
        if isValid(mid):
            high = mid
        else:
            low = mid
            
    return round(high, 6)

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 9
print(f"Kết quả: {minimize_Max_Distance(x, k)}")