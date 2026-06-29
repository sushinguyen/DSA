class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if self.isEmpty():
            raise IndexError("Stack rong!")
        return self.data.pop()

    def top(self):
        if self.isEmpty():
            raise IndexError("Stack rong!")
        return self.data[-1]

    def isEmpty(self):
        return len(self.data) == 0


s = Stack()
s.push(1)
s.push(2)
s.push(3)

print("Top:", s.top())
print("Pop:", s.pop())
print("Pop:", s.pop())
print("Empty?", s.isEmpty())
