def vitrixuathiendautien(x,a):
    left = 0
    right = len(a) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            result = mid
            right = mid - 1
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return result
x = 2
a = [1, 2, 2, 2, 2, 3]
print(vitrixuathiendautien(x, a))