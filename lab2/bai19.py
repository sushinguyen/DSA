def count_cows(x, c):
    x.sort()
    
    left = 1
    right = x[-1] - x[0]
    ans = 0
    
    def can_place(dist):
        count = 1
        last_position = x[0]
        
        for i in range(1, len(x)):
            if x[i] - last_position >= dist:
                count += 1
                last_position = x[i]
                if count >= c:
                    return True
        return False

    while left <= right:
        mid = (left + right) // 2
        
        if can_place(mid):
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
            
    return ans

x = [1, 2, 4, 8, 9]
c = int(input("Nhập: "))
result = count_cows(x, c)

print(f"Khoảng cách lớn nhất giữa hai con bò gần nhau nhất là: {result}")