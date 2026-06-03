def timtrongmangxoay(a,x):
    left = 0
    right = len(a) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            return mid
        if a[left] <= a[mid]: 
            if a[left] <= x < a[mid]:
                    right = mid - 1
            else:
                    left = mid + 1
        else:
            if a[mid] < x <= a[right]:
                    left = mid + 1
            else:
                    right = mid - 1
    return -1
a = [4, 5, 6, 7, 0, 1, 2]
x = 0

vitri = timtrongmangxoay(a, x)
print(vitri)