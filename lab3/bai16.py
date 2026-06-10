def count_inversions(arr):
    n = len(arr)
    count = 0
    temp_arr = arr.copy()
    for i in range(n):
        for j in range(0, n - i - 1):
            if temp_arr[j] > temp_arr[j + 1]:
                temp_arr[j], temp_arr[j + 1] = temp_arr[j + 1], temp_arr[j]
                count += 1
    return count
a = [2,3,1]
print("so luong cap nguoc chieu:",count_inversions(a))