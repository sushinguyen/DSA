def vitrixuathiencuoicung(a, x):
    result = -1
    left, right = 0, len(a) - 1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            right = mid - 1
        else:
            left = mid + 1
    return result
x=2
a = [1,2,2,2,3]
print(vitrixuathiencuoicung(a, x))