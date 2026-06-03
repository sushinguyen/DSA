
import sys
arr = [140, 25, 15, 52, 10, 250, 55]
for i in range(len(arr)):
    min = i
    for j in range(i+1, len(arr)):
        if arr[min] > arr[j]:
            min = j
    #Đổi chỗ phần tử
    arr[i], arr[min] = arr[min], arr[i]
print ("Sorted array")
for i in range(len(arr)):
    print("%d" %arr[i])