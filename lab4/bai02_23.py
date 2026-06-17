def phan_tich(a):
    a = a[:]
    n = len(a)
    dem_ss = dem_swap = 0
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            dem_ss += 1
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            dem_swap += 1
    return dem_ss, dem_swap

n = 5
best  = list(range(n))
avg   = [3, 1, 4, 5, 2]
worst = list(range(n - 1, -1, -1))

for label, arr in [("Best ", best), ("Avg  ", avg), ("Worst", worst)]:
    ss, sw = phan_tich(arr)
    print(f"{label}: so sanh={ss}, swap={sw}")
