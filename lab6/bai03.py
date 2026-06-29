class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if self.isEmpty():
            raise IndexError("Underflow Stack rong.")
        return self.data.pop()

    def isEmpty(self):
        return len(self.data) == 0

    def __repr__(self):
        return str(self.data[::-1])


def simulate(commands):
    stack = Stack()
    for cmd in commands:
        parts = cmd.strip().split()
        if parts[0] == "push":
            value = int(parts[1])
            stack.push(value)
            print(f"push {value} {stack}")
        elif parts[0] == "pop":
            val = stack.pop()
            print(f"pop {val} con lai: {stack}")
    print(f"Trang thai cuoi: {stack}")


commands = ["push 5", "push 7", "pop"]
simulate(commands)
