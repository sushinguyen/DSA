import random
import copy

def insertion_sort_stats(arr):
    comparisons = 0
    shifts = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                shifts += 1
                j -= 1
            else:
                break
        arr[j + 1] = key
    return comparisons, shifts

def bubble_sort_stats(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                swapped = True
        if not swapped: 
            break
    return comparisons, swaps

def selection_sort_stats(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[min_idx] > arr[j]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
    return comparisons, swaps
original_data = [random.randint(1, 10000) for _ in range(1000)]
data1 = copy.deepcopy(original_data)
data2 = copy.deepcopy(original_data)
data3 = copy.deepcopy(original_data)

comp_ins, shift_ins = insertion_sort_stats(data1)
comp_bub, swap_bub = bubble_sort_stats(data2)
comp_sel, swap_sel = selection_sort_stats(data3)

print(f"{'Thuật toán':<20} | {'Số lần so sánh':<15} | {'Số lần đổi chỗ/Shift':<20}")
print("-" * 60)
print(f"{'Insertion Sort':<20} | {comp_ins:<15} | {shift_ins:<20}")
print(f"{'Bubble Sort':<20} | {comp_bub:<15} | {swap_bub:<20}")
print(f"{'Selection Sort':<20} | {comp_sel:<15} | {swap_sel}")