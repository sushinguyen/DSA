def dua_ve_dau(a):
    min_idx = 0
    for i in range(1, len(a)):
        if a[i] < a[min_idx]:
            min_idx = i
    a[0], a[min_idx] = a[min_idx], a[0]
    return a

a = [4, 2, 7, 1, 3]
print(dua_ve_dau(a))