
def bubble_sort(arr):
    n = len(arr)
    for i in range(min(k,n)):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            return False
    return True
a = [3,2,1]
k = 1
print("check k luot:",bubble_sort(a))