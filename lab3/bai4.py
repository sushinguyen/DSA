def count (arr):
    a = arr.copy()
    n = len(a)
    swap_count = 0
    
    for i in range(n):
        for j in range(0, n-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swap_count += 1
    return swap_count

arr = [3,2,1,7,5]
print("Số lần hoán đổi cần thiết để sắp xếp mảng:", count(arr))