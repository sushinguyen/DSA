def selection_sort_dem_sosánh(a):
    n = len(a)
    dem = 0
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            dem += 1
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a, dem

a = [5, 3, 1, 4, 2]
mang, so_ss = selection_sort_dem_sosánh(a)
print(mang, "so sánh:", so_ss)