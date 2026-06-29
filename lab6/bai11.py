def next_greater_element(arr):
    n = len(arr)
    result = [-1] * n
    stack = []

    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            idx = stack.pop()
            result[idx] = arr[i]
        stack.append(i)

    return result


print(next_greater_element([2, 1, 3]))
print(next_greater_element([4, 3, 2, 1]))
print(next_greater_element([1, 3, 2, 4]))
print(next_greater_element([1]))