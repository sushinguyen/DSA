import random
def count_shifts_insertion_sort(arr):
    shifts = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            shifts += 1
            j -= 1
        arr[j + 1] = key
    return shifts
n = 10000
k = 3
k_deviated_array = list(range(n))
for i in range(n - k):
    swap_idx = i + random.randint(1, k)
    k_deviated_array[i], k_deviated_array[swap_idx] = k_deviated_array[swap_idx], k_deviated_array[i]

shifts = count_shifts_insertion_sort(k_deviated_array)
print(f"Số shift thực tế trên mảng kích thước {n}, độ lệch k={k}: {shifts}")
