from collections import deque

def reverse_queue(queue):
    stack = []
    while queue:
        stack.append(queue.popleft())
    while stack:
        queue.append(stack.pop())
    return queue


q = deque([1, 2, 3])
print(list(reverse_queue(q)))

q2 = deque([10, 20, 30, 40, 50])
print(list(reverse_queue(q2)))
