def count(arr):
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(0, n-1-i):
            if arr[j] > arr[j+1]:
                count += 1 
    return count
arr = [3,2,1,7,5]
print("Số lần hoán đổi cần thiết để sắp xếp mảng:", count(arr))