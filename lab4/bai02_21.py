# Bài 21. Chứng minh số so sánh cố định
# Chứng minh: tổng so sánh = n*(n-1)/2, không đổi theo đầu vào

def dem_so_sanh(a):
    n = len(a)
    dem = 0
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            dem += 1
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return dem

from itertools import permutations
n = 4
ket_qua = {dem_so_sanh(list(p)) for p in permutations(range(n))}
print("Tap hop so so sanh:", ket_qua)       # {6}
print("n*(n-1)/2 =", n * (n - 1) // 2)     # 6
