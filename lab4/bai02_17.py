# Bài 17. Phần tử nhỏ thứ k (partial selection)
# Ví dụ: a = [7, 2, 5, 1, 9], k = 3 → 5

def phan_tu_nho_thu_k(a, k):
    a = a[:]
    for i in range(k):
        min_idx = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a[k - 1]

a = [7, 2, 5, 1, 9]
print(phan_tu_nho_thu_k(a, 3))  # 5
# Do phuc tap: O(n*k)
