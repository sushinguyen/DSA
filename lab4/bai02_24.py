
import heapq
import time, random

def k_nho_nhat_selection(a, k):
    a = a[:]
    for i in range(k):
        min_idx = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a[:k]

def k_nho_nhat_heap(a, k):
    return heapq.nsmallest(k, a)

n = 10000
a = random.sample(range(n * 10), n)

for k in [5, 50, 500]:
    t1 = time.perf_counter()
    k_nho_nhat_selection(a, k)
    t1 = time.perf_counter() - t1

    t2 = time.perf_counter()
    k_nho_nhat_heap(a, k)
    t2 = time.perf_counter() - t2

    print(f"k={k:4d}: selection={t1:.4f}s, heap={t2:.4f}s")
