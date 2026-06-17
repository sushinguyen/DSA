# Bài 9. Double selection sort
# Ví dụ: a = [5, 1, 4, 2, 8] → [1, 2, 4, 5, 8]

def double_selection_sort(a):
    n = len(a)
    left, right = 0, n - 1
    while left < right:
        min_idx = max_idx = left
        for j in range(left + 1, right + 1):
            if a[j] < a[min_idx]:
                min_idx = j
            if a[j] > a[max_idx]:
                max_idx = j
        a[left], a[min_idx] = a[min_idx], a[left]
        if max_idx == left:
            max_idx = min_idx
        a[right], a[max_idx] = a[max_idx], a[right]
        left += 1
        right -= 1
    return a

a = [5, 1, 4, 2, 8]
print(double_selection_sort(a))  # [1, 2, 4, 5, 8]
