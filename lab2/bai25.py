def max_Distance(x, m):
    x.sort()
    
    def isValid(mid):
        count = 1
        last_positioned = x[0]
        
        for i in range(1, len(x)):
            if x[i] - last_positioned >= mid:
                count += 1
                last_positioned = x[i]
                
                if count >= m:
                    return True
        return False

    low = 1
    high = x[-1] - x[0]
    ans = 0
    
    while low <= high:
        mid = (low + high) // 2
        
        if isValid(mid):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
            
    return ans

x = [1, 2, 3, 4, 7]
m = 3
print(f"Khoảng cách lớn nhất có thể đạt được: {max_Distance(x, m)}")