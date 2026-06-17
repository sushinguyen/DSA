def selection_sort_dem_swap(a):
    n = len(a)
    dem = 0
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            dem += 1
    return a, dem

a = [3, 2, 1]
mang, so_swap = selection_sort_dem_swap(a)
print(mang, "swap:", so_swap)  