import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def enqueue(self, value, priority):
        heapq.heappush(self.heap, (priority, value))

    def dequeue(self):
        if self.isEmpty():
            print("Underflow!")
            return None
        priority, value = heapq.heappop(self.heap)
        return value, priority

    def front(self):
        if self.isEmpty():
            return None
        return self.heap[0]

    def isEmpty(self):
        return len(self.heap) == 0


pq = PriorityQueue()
pq.enqueue("viec C", 3)
pq.enqueue("viec A", 1)
pq.enqueue("viec B", 2)

print(pq.dequeue())
print(pq.dequeue())
print(pq.dequeue())
