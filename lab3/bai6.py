def last_e_onepass (arr):
    if not arr: return None
    a = arr.copy()
    n = len(a)
    for i in range(0, n-1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
    return a[n-1]
arr = [4,2,7,1,3]
print("Phần tử lớn nhất sau một lần duyệt:", last_e_onepass(arr))