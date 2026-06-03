def timphantudonle(mang):
    low = 0
    high = len(mang) - 1
    
    while low < high:
        mid = (low + high) // 2
        if mid % 2 == 0:
            if mang[mid] == mang[mid + 1]:
                low = mid + 2
            else:
                high = mid
        else:
            if mang[mid] == mang[mid - 1]:
                low = mid + 1
            else:
                high = mid - 1
                
    return mang[low]

a = [1, 1, 2, 3, 3, 4, 4]
phantu = timphantudonle(a)
print(phantu)