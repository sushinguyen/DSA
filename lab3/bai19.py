def min_passes(arr):
    n = len(arr)
    temp_arr = arr.copy()
    passes = 0
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if temp_arr[j] > temp_arr[j + 1]:
                temp_arr[j], temp_arr[j + 1] = temp_arr[j + 1], temp_arr[j]
                swapped = True
        
        if swapped:
            passes += 1
        else:
            break
            
    return passes
a = [1, 2, 3, 5, 4]
print("so lan sap xep:", min_passes(a))
