def count_shifts_fast(arr):
    if len(arr) <= 1:
        return arr, 0
        
    mid = len(arr) // 2
    left_arr, left_inv = count_shifts_fast(arr[:mid])
    right_arr, right_inv = count_shifts_fast(arr[mid:])
    
    merged_arr = []
    i = j = 0
    split_inv = 0
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            merged_arr.append(left_arr[i])
            i += 1
        else:
            merged_arr.append(right_arr[j])
            split_inv += (len(left_arr) - i) 
            j += 1
            
    merged_arr.extend(left_arr[i:])
    merged_arr.extend(right_arr[j:])
    
    total_inv = left_inv + right_inv + split_inv
    return merged_arr, total_inv
c = [2, 4, 1, 3, 5]
_, total_shifts = count_shifts_fast(c)
print(f"Mảng: {c}")
print(f"Tổng số shift (tính bằng Merge Sort O(n log n)): {total_shifts}")