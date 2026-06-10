def sort_student(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j][1] < arr[j+1][1] or (arr[j][1] == arr[j+1][1] and arr[j][0] > arr[j+1][0]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
students = [('An', 8), ('Ba', 9), ('Cu', 8)]
sorted_students = sort_student(students)
print("Danh sách sinh viên sau khi sắp xếp:", sorted_students)