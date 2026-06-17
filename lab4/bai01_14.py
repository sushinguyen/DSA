def should_shift(item_j, key):
    if item_j[1] < key[1]: 
        return True
    elif item_j[1] == key[1]:
        if item_j[0] > key[0]:
            return True
    return False

def insertion_sort_multi_keys(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and should_shift(arr[j], key):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

print (should_shift([('An',8), ('Ba',9), ('Cu',8)]))