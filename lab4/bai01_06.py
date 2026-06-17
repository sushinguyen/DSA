def insertion_sort_count_comparisons(arr):
    comparisons = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0:
            comparisons += 1
            if key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
                
        arr[j + 1] = key
        
    return comparisons
print(insertion_sort_count_comparisons([1, 2, 3]))
