def early_exit (arr):
    n = len(arr)
    count = 0
    for i in range (n):
        swapped = False
        count += 1
        for j in range (0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return count
a = [1,2,3,4]
so_luot = early_exit(a)
print("so luot sap xep:",so_luot)