def giatrinhonhat(a):
    left = 0
    right = len(a) - 1
    while left < right:
        mid = (left + right) // 2
        if a[mid] > a[right]:
            right = mid
        else:
            left = mid + 1
    return a[left]
a = [3, 4, 5, 1, 2]
giatri = giatrinhonhat(a)
print(giatri)