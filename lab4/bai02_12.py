# Bài 12. Selection sort ổn định
# Ví dụ: giữ nguyên thứ tự phần tử cùng khóa

def selection_sort_on_dinh(a):
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j][0] < a[min_idx][0]:
                min_idx = j
        key = a[min_idx]
        while min_idx > i:
            a[min_idx] = a[min_idx - 1]
            min_idx -= 1
        a[i] = key
    return a

a = [(2, 'a'), (2, 'b'), (1, 'c')]
print("Truoc:", a)
print("Sau:  ", selection_sort_on_dinh(a))
# [(1,'c'), (2,'a'), (2,'b')] → (2,'a') vẫn trước (2,'b') ✅
