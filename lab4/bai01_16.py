class OnlineInsertionSort:
    def __init__(self):
        self.arr = []
        
    def insert_new_element(self, element):
        self.arr.append(element)
        j = len(self.arr) - 2
        while j >= 0 and self.arr[j] > element:
            self.arr[j + 1] = self.arr[j]
            j -= 1
            
        self.arr[j + 1] = element
        return self.arr
stream = OnlineInsertionSort()
luong_du_lieu = [5, 2, 8, 1]

print("Quá trình nhận dữ liệu:")
for val in luong_du_lieu:
    print(f"Thêm {val}: {stream.insert_new_element(val)}")