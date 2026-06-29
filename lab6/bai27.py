from collections import deque

def josephus(n, k):
    queue = deque(range(1, n + 1))
    while len(queue) > 1:
        for _ in range(k - 1):
            queue.append(queue.popleft())
        queue.popleft()
    return queue[0]


print(josephus(5, 2))
print(josephus(7, 3))
print(josephus(6, 1))
