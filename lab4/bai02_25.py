def selection_sort(a):
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a
from itertools import permutations
for perm in permutations([3, 1, 4, 1, 5]):
    assert selection_sort(list(perm)) == [1, 1, 3, 4, 5]
print("Tat ca hoan vi deu dung")
