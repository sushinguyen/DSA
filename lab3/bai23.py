import random

def profile_bubble_sort(arr):
    n = len(arr)
    comps = 0
    swaps = 0
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comps += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                swapped = True
        if not swapped:
            break
    return comps, swaps
n = 1000
arr_sorted = list(range(n))
arr_reverse = list(range(n, 0, -1))
arr_random = random.sample(range(n * 2), n)
c1, s1 = profile_bubble_sort(arr_sorted)
c2, s2 = profile_bubble_sort(arr_random)
c3, s3 = profile_bubble_sort(arr_reverse)
print(f"{'Loại đầu vào':<15} | {'So sánh':<10} | {'Hoán đổi':<10} | {'Độ phức tạp':<15}")
print(f"{'Đã sắp xếp':<15} | {c1:<10} | {s1:<10} | O(n)")
print(f"{'Ngẫu nhiên':<15} | {c2:<10} | {s2:<10} | O(n^2)")
print(f"{'Ngược lại':<15} | {c3:<10} | {s3:<10} | O(n^2)")  