def largest_rectangle(heights):
    stack = []
    max_area = 0
    n = len(heights)

    for i in range(n + 1):
        h = 0 if i == n else heights[i]
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)

    return max_area


print(largest_rectangle([2, 1, 5, 6, 2, 3]))
print(largest_rectangle([2, 4]))
print(largest_rectangle([1, 1, 1, 1]))
print(largest_rectangle([6, 2, 5, 4, 5, 1, 6]))