def insertion_sort_k_steps(arr, k):
    for i in range(1, min(k + 1, len(arr))):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
k = 1
print(insertion_sort_k_steps([4, 3, 2, 1],k))