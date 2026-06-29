class QueueUsingTwoStacks:
    def __init__(self):
        self.in_stack  = []
        self.out_stack = []

    def enqueue(self, value):
        self.in_stack.append(value)

    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        if not self.out_stack:
            print("Underflow!")
            return None
        return self.out_stack.pop()

    def front(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1] if self.out_stack else None


q = QueueUsingTwoStacks()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
q.enqueue(4)
print(q.dequeue())
print(q.dequeue())
