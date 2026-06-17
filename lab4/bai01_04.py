def insertion_sort_print_steps(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(f"Bước {i}: {arr}")

print(insertion_sort_print_steps([3, 1, 2]))