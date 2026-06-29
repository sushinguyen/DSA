class MinStack:
    def __init__(self):
        self.main_stack = []
        self.min_stack  = []

    def push(self, value):
        self.main_stack.append(value)
        if self.min_stack:
            self.min_stack.append(min(value, self.min_stack[-1]))
        else:
            self.min_stack.append(value)
        print(f"push({value}) -> main: {self.main_stack} | min_stack: {self.min_stack}")

    def pop(self):
        if self.isEmpty():
            print("Underflow!")
            return None
        val = self.main_stack.pop()
        self.min_stack.pop()
        print(f"pop() -> lay ra: {val} | min_stack: {self.min_stack}")
        return val

    def top(self):
        return self.main_stack[-1] if not self.isEmpty() else None

    def getMin(self):
        if self.isEmpty():
            print("Stack rong!")
            return None
        return self.min_stack[-1]

    def isEmpty(self):
        return len(self.main_stack) == 0


print("Test 1: push 5,3,7 -> getMin = 3")
s = MinStack()
s.push(5)
s.push(3)
s.push(7)
print(f"getMin() = {s.getMin()}")

print("\nTest 2: min tu khoi phuc sau pop")
s2 = MinStack()
s2.push(5)
s2.push(3)
s2.push(7)
print(f"getMin() = {s2.getMin()}")
s2.pop()
s2.pop()
print(f"getMin() = {s2.getMin()}")
