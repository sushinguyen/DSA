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

arr_bai17 = [1, 2, 4, 3, 5]
print(f"Bài 17 - Mảng gần sắp xếp {arr_bai17}: Số shift = {count_shifts_insertion_sort(arr_bai17)}") 
