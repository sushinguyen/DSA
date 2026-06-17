
def selection_sort_swap_chinh_xac(a):
    n = len(a)
    dem_swap = 0
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            dem_swap += 1
    return a, dem_swap

print(selection_sort_swap_chinh_xac([1, 2, 3]))
print(selection_sort_swap_chinh_xac([3, 2, 1]))
print(selection_sort_swap_chinh_xac([3, 1, 2]))
