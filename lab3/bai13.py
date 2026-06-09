def bs_stable(a):
    n = len(a)
    arr = a.copy()
    for i in range(n):
        swapped = False
        for j in range (0, n-i-1):
            if arr[j][0] > arr[j+1][0]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
a = [(2, 'a'), (1, 'b'), (2, 'c')]
kq = bs_stable(a)
print("mang sau khi sap xep:",kq)