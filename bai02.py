def kiemtratontai (a,x):

    left = 0
    right = len(a) - 1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return False   
x =5
a = [2, 4, 6, 8]
print(kiemtratontai(a, x))
