# Bài 11. Tính KHÔNG ổn định
# Ví dụ: [(2,'a'),(2,'b'),(1,'c')] → có thể đổi thứ tự a, b

def selection_sort_khong_on_dinh(a):
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j][0] < a[min_idx][0]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

a = [(2, 'a'), (2, 'b'), (1, 'c')]
print("Truoc:", a)
print("Sau:  ", selection_sort_khong_on_dinh(a))
# (2,'b') xuất hiện trước (2,'a') → không ổn định!
