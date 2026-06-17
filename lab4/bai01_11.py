def insertion_sort_abs(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # So sánh dựa trên giá trị tuyệt đối: abs()
        while j >= 0 and abs(arr[j]) > abs(key):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

print(insertion_sort_abs([-3, 1, -2, 2]))