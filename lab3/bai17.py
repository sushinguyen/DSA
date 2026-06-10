def partial (arr, k):
    n = len(arr)
    for i in range(k):
        swapped = False
        for j in range (0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
a = [3, 1, 4, 1, 5]
k = 2
print("k phan tu nho nhat:",partial(a, k))