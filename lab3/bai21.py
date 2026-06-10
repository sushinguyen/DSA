def stable_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j][0] > arr[j + 1][0]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
def unstable_selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j][0] < arr[min_idx][0]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
data = [(2, 'A_trước'), (1, 'B'), (2, 'C_sau'), (1, 'D')]

data_bubble = data.copy()
data_selection = data.copy()
print("Trước khi sắp xếp:")
print("Bubble Sort:", data_bubble) 
print("Selection Sort:", data_selection)