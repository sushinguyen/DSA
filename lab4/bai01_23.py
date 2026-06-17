import random
def analyze_insertion_sort(arr):
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

n_test = 1000


best_arr = list(range(n_test))
best_comp, best_shift = analyze_insertion_sort(best_arr)

worst_arr = list(range(n_test, 0, -1))
worst_comp, worst_shift = analyze_insertion_sort(worst_arr)

avg_arr = random.sample(range(n_test * 10), n_test)
avg_comp, avg_shift = analyze_insertion_sort(avg_arr)

print(f"Kích thước mảng N = {n_test}")
print("-" * 50)
print(f"{'Trường hợp':<15} | {'Số So Sánh':<15} | {'Số Shift':<15}")
print("-" * 50)
print(f"{'Best Case':<15} | {best_comp:<15} | {best_shift:<15}")
print(f"{'Average Case':<15} | {avg_comp:<15} | {avg_shift:<15}")
print(f"{'Worst Case':<15} | {worst_comp:<15} | {worst_shift:<15}")