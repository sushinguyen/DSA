class BoundedStack:
    def __init__(self, maxSize):
        self.data = []
        self.maxSize = maxSize

    def push(self, value):
        if self.isFull():
            print(f"OVERFLOW Stack da day (max={self.maxSize}), khong the push {value}")
            return False
        self.data.append(value)
        print(f"push {value} {self.data}")
        return True

    def pop(self):
        if self.isEmpty():
            print("UNDERFLOW Stack dang rong, khong the pop")
            return None
        val = self.data.pop()
        print(f"pop lay ra {val}  con lai {self.data}")
        return val

    def top(self):
        if self.isEmpty():
            print("Stack rong, khong co dinh")
            return None
        return self.data[-1]

    def isEmpty(self):
        return len(self.data) == 0

    def isFull(self):
        return len(self.data) == self.maxSize


print("Test OVERFLOW")
s = BoundedStack(maxSize=3)
s.push(10)
s.push(20)
s.push(30)
s.push(99)

print("\nTest UNDERFLOW")
s2 = BoundedStack(maxSize=3)
s2.pop()
s2.push(5)
s2.pop()
s2.pop()
