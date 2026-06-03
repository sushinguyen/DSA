def binary_search(arr, key):
    left = 0
    right = len(arr) - 1
    step = 0
    
    print(f"\n--- Bắt đầu tìm kiếm key = {key} ---")
    
    while left <= right:
        step += 1
        mid = (left + right) // 2
        print(f"Bước {step}: left={left}, right={right}, mid={mid} -> Giá trị arr[mid]={arr[mid]}")
        
        if arr[mid] == key:
            return mid
            
        if key < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
            
    return -1

arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]

x_a = 95
result_a = binary_search(arr, x_a)
if result_a != -1:
    print(f"=> Kết quả câu a: Tìm thấy {x_a} tại vị trí i = {result_a}")
else:
    print(f"=> Kết quả câu a: Không tìm thấy phần tử {x_a} trong mảng (Trả về {result_a})")


x_b = 5
result_b = binary_search(arr, x_b)
if result_b != -1:
    print(f"=> Kết quả câu b: Tìm thấy {x_b} tại vị trí i = {result_b}")
else:
    print(f"=> Kết quả câu b: Không tìm thấy phần tử {x_b} trong mảng (Trả về {result_b})")