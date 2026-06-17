# Bài 16. Sắp xếp theo trị tuyệt đối
# Ví dụ: a = [-3, 1, -2, 2] → [1, -2, 2, -3]

def selection_sort_abs(a):
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if abs(a[j]) < abs(a[min_idx]):
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

a = [-3, 1, -2, 2]
print(selection_sort_abs(a))  # [1, -2, 2, -3]
