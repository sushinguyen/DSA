import math

def binary_search(arr, key):            # Khai báo hàm tìm kiếm nhị phân
    mid = 0                             # Khởi tạo vị trí ở giữa
    left = 0                            # Khởi tạo chỉ số đầu mảng
    right = len(arr) - 1                # Sửa lại thành len(arr) - 1 để tránh lỗi vượt quá chỉ số mảng
    step = 0                            # Khởi tạo biến đếm số bước lặp
    
    while (left <= right):              # Vòng lặp điều kiện: chạy khi khoảng tìm kiếm còn hợp lệ
        step = step + 1                 # Tăng số bước lặp lên 1
        mid = (left + right) // 2       # Tính vị trí phần tử ở giữa hiện tại
        
        if (key == arr[mid]):           # Nếu tìm thấy phần tử cần tìm tại vị trí mid
            return mid                  # Trả về chỉ số tìm thấy
            
        if (key < arr[mid]):            # Nếu phần tử cần tìm nhỏ hơn phần tử ở giữa
            right = mid - 1             # Thu hẹp phạm vi tìm kiếm sang nửa bên trái
        else:                           # Nếu phần tử cần tìm lớn hơn phần tử ở giữa
            left = mid + 1              # Thu hẹp phạm vi tìm kiếm sang nửa bên phải
            
    return -1                           # Trả về -1 nếu không tìm thấy key trong mảng

arr = [0, 4, 5, 9, 13, 15, 18, 24, 28, 29, 35]
key = 40
result = binary_search(arr, key)
print("Vi tri tim kiem thu i la:", result)