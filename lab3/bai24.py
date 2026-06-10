def find_passes_between_states(initial_arr, current_arr):
    initial_pos = {val: idx for idx, val in enumerate(initial_arr)}
    
    max_left_shift = 0
    for current_idx, val in enumerate(current_arr):
        start_idx = initial_pos[val]
        if start_idx > current_idx:
            left_shift = start_idx - current_idx
            max_left_shift = max(max_left_shift, left_shift)
            
    return max_left_shift

dau = [4, 3, 2, 1]
sau = [3, 2, 1, 4]
so_luot = find_passes_between_states(dau, sau)
print(f" Đã thực hiện ít nhất {so_luot} lượt")