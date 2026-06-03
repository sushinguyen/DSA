def sodautien(a,x):
    left, right = 0, len(a) - 1
    first_pos = -1
    while left <= right:
        mid = left + (right - left) // 2
        if a[mid] == x:
            first_pos = mid
            right = mid - 1
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return first_pos
def socuoicung(a,x):
    left, right = 0, len(a) - 1
    last_pos = -1
    while left <= right:
        mid = left + (right - left) // 2
        if a[mid] == x:
            last_pos = mid
            left = mid + 1
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return last_pos
def demso(a,x):
    first_pos = sodautien(a,x)
    if first_pos == -1:
        return 0
    last_pos = socuoicung(a,x)
    return last_pos - first_pos + 1
x=2
a = [1,2,2,2,3]
print(demso(a,x))