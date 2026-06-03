def canbac2(n):
    if n ==0 or n ==1:
        return n
    left = 1
    right = n
    ans = 0

    while left <= right:    
        mid = (left + right) // 2
        if mid * mid <= n:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    return ans
n = 8
n = 16
print(f" n = 8: {canbac2(8)}")
print(f" n = 16: {canbac2(16)}")