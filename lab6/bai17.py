class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data  = [None] * capacity
        self.front = 0
        self.rear  = -1
        self.size  = 0

    def enqueue(self, value):
        if self.isFull():
            print("Overflow!")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.data[self.rear] = value
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            print("Underflow!")
            return None
        val = self.data[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return val

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity


cq = CircularQueue(4)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)
cq.enqueue(5)
print(cq.dequeue())
cq.enqueue(5)
print(cq.dequeue())
print(cq.dequeue())
print(cq.dequeue())
print(cq.dequeue())
