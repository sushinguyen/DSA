def bs_abs (a):
    n = len(a)
    arr = a.copy()
    for i in range(n):
        swapped = False
        for j in range (0, n-i-1):
            if abs(arr[j]) > abs(arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
a = [-3, 1, -2, 2]
kq = bs_abs(a)
print("mang sau khi sap xep:",kq)