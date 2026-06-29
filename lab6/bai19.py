from collections import deque

class BoundedQueue:
    def __init__(self, capacity):
        self.data = deque()
        self.capacity = capacity

    def enqueue(self, value):
        if self.isFull():
            print(f"Overflow! Khong the enqueue {value}")
            return
        self.data.append(value)
        print(f"enqueue {value} -> {list(self.data)}")

    def dequeue(self):
        if self.isEmpty():
            print("Underflow! Queue rong")
            return None
        val = self.data.popleft()
        print(f"dequeue -> {val} | con lai: {list(self.data)}")
        return val

    def isEmpty(self):
        return len(self.data) == 0

    def isFull(self):
        return len(self.data) == self.capacity

    def count(self):
        return len(self.data)


q = BoundedQueue(3)
q.dequeue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(f"So phan tu: {q.count()}")
q.dequeue()
print(f"So phan tu: {q.count()}")
