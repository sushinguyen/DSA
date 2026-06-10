def test_nearly_sorted_array(arr):
    n = len(arr)
    passes = 0
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if swapped:
            passes += 1
        else:
            break
    return passes
a = [3, 1, 2, 6, 4, 5] 
passes = test_nearly_sorted_array(a)
print("so lan sap xep:", passes)