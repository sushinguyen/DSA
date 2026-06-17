def shell_sort(arr):
    n = len(arr)
    gap = n // 2 
    
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
            
        gap //= 2  
    return arr
b = [8, 4, 1, 56, 3, -44, 23, -6, 28, 0]
print(f"Shell Sort: {shell_sort(b)}")