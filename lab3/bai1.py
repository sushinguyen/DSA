#Bài 1. Thực hiện một lượt (one pass)
#Cho mảng a. Thực hiện đúng một lượt của bubble sort (duyệt từ trái sang phải, hoán đổi cặp
#liền kề nếu sai thứ tự tăng dần) và in ra mảng sau lượt đó.
def onepass (arr):
    n = len(arr)
    for j in range(0, n-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
arr = [5,1,4,2,8]
print("Mảng sau khi thực hiện một lượt bubble sort:", onepass(arr)) 