def count_inversions(arr):
    inversions = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inversions += 1
    return inversions

def count_insertion_sort_shifts(arr):
    arr_copy = arr.copy() 
    shifts = 0
    for i in range(1, len(arr_copy)):
        key = arr_copy[i]
        j = i - 1
        while j >= 0 and arr_copy[j] > key:
            arr_copy[j + 1] = arr_copy[j]
            shifts += 1
            j -= 1
        arr_copy[j + 1] = key
    return shifts

a = [2, 4, 1, 3]

so_nghich_the = count_inversions(a)
so_shift = count_insertion_sort_shifts(a)

print(f"Mảng ban đầu: {a}")
print(f"Số nghịch thế tính theo định nghĩa: {so_nghich_the}")
print(f"Số lần shift thực tế khi chạy thuật toán: {so_shift}")