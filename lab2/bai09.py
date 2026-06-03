def vitrichen(a, x):
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
    return left
a = [1, 3, 5, 6]
x = 4
vitri = vitrichen(a, x)
print(vitri)