class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Queue rong!")
        return self.data.pop(0)

    def front(self):
        if self.isEmpty():
            raise IndexError("Queue rong!")
        return self.data[0]

    def isEmpty(self):
        return len(self.data) == 0


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.front())
print(q.isEmpty())
