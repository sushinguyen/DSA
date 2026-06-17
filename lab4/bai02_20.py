# Bài 20. Liên hệ với heap sort
# selection O(n²) → heap sort O(n log n)

import heapq

def selection_sort(a):
    a = a[:]
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

def heap_sort(a):
    a = a[:]
    heapq.heapify(a)
    return [heapq.heappop(a) for _ in range(len(a))]

a = [5, 1, 4, 2, 8, 3]
print("Selection:", selection_sort(a))
print("Heap:     ", heap_sort(a))
