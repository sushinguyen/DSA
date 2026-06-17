def selection_sort_on_dinh_inplace(a):
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        key = a[min_idx]
        while min_idx > i:
            a[min_idx] = a[min_idx - 1]
            min_idx -= 1
        a[i] = key
    return a

a = [(2, 'a'), (1, 'b'), (2, 'c'), (1, 'd')]
print(selection_sort_on_dinh_inplace(a))