
def selection_Sort(array, n):
    
    for index in range(n):
        min_index = index
        
        for j in range(index + 1, n):
            if array[j] < array[min_index]:
                min_index = j
        (array[index], array[min_index]) = (array[min_index], array[index])

arr = [-25, 40, 0, 15, -90,80,-92,-210,747,500,1050,999]
n = len(arr)
selection_Sort(arr, n)
print('array sau khi sắp xếp là:')
print(arr)