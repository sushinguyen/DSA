def insertion_sort_length(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # So sánh dựa trên độ dài chuỗi
        while j >= 0 and len(arr[j]) > len(key):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
print (insertion_sort_length(['abc', 'a', 'ab']))