# Bài 15. Sắp xếp một phần (k nhỏ nhất)
# Ví dụ: a = [5, 3, 1, 4, 2], k = 2 → [1, 2, ...]

def partial_selection_sort(a, k):
    n = len(a)
    for i in range(k):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

a = [5, 3, 1, 4, 2]
print(partial_selection_sort(a, 2))  # [1, 2, 5, 4, 3]
