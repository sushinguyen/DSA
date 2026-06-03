
arr = [64, 34, 25, 5, 22, 11, 90, 12, -15,-50,100]

n = len(arr)
for i in range(n-1):
    min_index = i
    for j in range(i+1, n):
        if arr[j] < arr[min_index]:
            min_index = j
    min_value = arr.pop(min_index)
    arr.insert(i, min_value)
print("Sorted array:", arr)