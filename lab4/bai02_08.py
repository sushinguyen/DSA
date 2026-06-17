
def tim_chi_so_nho_nhat(a, i):
    min_idx = i
    for j in range(i + 1, len(a)):
        if a[j] < a[min_idx]:
            min_idx = j
    return min_idx

def selection_sort(a):
    n = len(a)
    for i in range(n):
        min_idx = tim_chi_so_nho_nhat(a, i)
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

a = [9, 3, 7, 1, 5]
print(tim_chi_so_nho_nhat(a, 1))
print(selection_sort(a))          
