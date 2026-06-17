def insertion_sort_swap(list_a, x):
    list_a.append(x)
    i = len(list_a) - 1
    while list_a[i-1] > list_a[i] and i > 0:
        list_a[i], list_a[i-1] = list_a[i-1], list_a[i]
        i = i-1
    return list_a
x = 4
list_a = [1, 3, 5, 7]
print(insertion_sort_swap(list_a, x))