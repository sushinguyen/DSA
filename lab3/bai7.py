#SAP XEP MANG KY TU DUNG BUBBLE SORT
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
a = ['d','a','c','b']
print("mang ky tu duoc sap xep:",bubble_sort(a))