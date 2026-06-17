# Bài 18. So sánh số swap với bubble sort
# Ví dụ: selection thường ít swap hơn bubble

def selection_sort_swap(a):
    a = a[:]
    n, dem = len(a), 0
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            dem += 1
    return a, dem

def bubble_sort_swap(a):
    a = a[:]
    n, dem = len(a), 0
    for i in range(n):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                dem += 1
    return a, dem

a = [5, 3, 4, 1, 2]
_, s_swap = selection_sort_swap(a)
_, b_swap = bubble_sort_swap(a)
print(f"Selection swap: {s_swap}")
print(f"Bubble swap:    {b_swap}")
