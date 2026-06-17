def gnome_sort(arr):
    pos = 0
    while pos < len(arr):
        if pos == 0 or arr[pos] >= arr[pos - 1]:
            pos += 1
        else:
            # Hoán vị và lùi lại
            arr[pos], arr[pos - 1] = arr[pos - 1], arr[pos]
            pos -= 1
    return arr

print(gnome_sort([3, 2, 1]))