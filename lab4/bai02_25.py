# Bài 25. Chứng minh tính đúng đắn (loop invariant)
# Invariant: trước vòng i, a[0..i-1] chứa i phần tử nhỏ nhất đã sắp xếp

def selection_sort(a):
    n = len(a)
    for i in range(n):
        # INVARIANT: a[0..i-1] chứa i phần tử nhỏ nhất, đã sắp xếp
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
        # SAU SWAP: a[0..i] chứa i+1 phần tử nhỏ nhất, đã sắp xếp
    return a

# Kiểm chứng với mọi hoán vị
from itertools import permutations
for perm in permutations([3, 1, 4, 1, 5]):
    assert selection_sort(list(perm)) == [1, 1, 3, 4, 5]
print("Tat ca hoan vi deu dung ✅")
