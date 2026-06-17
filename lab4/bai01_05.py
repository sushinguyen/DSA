def insertion_sort_count_shifts(arr):
    shifts = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            shifts += 1 
            j -= 1
            
        arr[j + 1] = key
        
    return shifts
print (insertion_sort_count_shifts([3, 2, 1]))