def early_exit (arr):
    n = len(arr)
    count = 0
    for i in range(n):
        swapped = False
        count += 1
        for j in range (0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return count
a = [2,1,3,4]
print("so luot sap xep:",early_exit(a))