class Deque:
    def __init__(self):
        self.data = []

    def pushFront(self, value):
        self.data.insert(0, value)

    def pushBack(self, value):
        self.data.append(value)

    def popFront(self):
        if self.isEmpty():
            print("Underflow!")
            return None
        return self.data.pop(0)

    def popBack(self):
        if self.isEmpty():
            print("Underflow!")
            return None
        return self.data.pop()

    def isEmpty(self):
        return len(self.data) == 0

    def __repr__(self):
        return str(self.data)


dq = Deque()
dq.pushFront(1)
dq.pushBack(2)
dq.pushFront(0)
print(dq)
print(dq.popFront())
print(dq.popBack())
print(dq)
