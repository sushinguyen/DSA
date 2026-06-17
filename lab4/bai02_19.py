# Bài 19. Double-ended selection — phân tích
# Ví dụ: xử lý cẩn thận khi maxIdx = vị trí đầu

def double_selection_sort_phan_tich(a):
    n = len(a)
    left, right = 0, n - 1
    dem_vong = 0
    dem_ss = 0

    while left < right:
        dem_vong += 1
        min_idx = max_idx = left

        for j in range(left + 1, right + 1):
            dem_ss += 1
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

    print(f"So vong: {dem_vong}, So so sanh: {dem_ss}")
    return a

a = [5, 1, 4, 2, 8, 3]
print(double_selection_sort_phan_tich(a))
