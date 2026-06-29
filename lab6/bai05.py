class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if self.isEmpty():
            raise IndexError("Underflow!")
        return self.data.pop()

    def isEmpty(self):
        return len(self.data) == 0

    def __repr__(self):
        return str(self.data)


def display_and_count(stack):
    aux = Stack()
    count = 0
    print("Duyet (LIFO): ", end="")
    while not stack.isEmpty():
        val = stack.pop()
        print(val, end="  ")
        aux.push(val)
        count += 1
    print(f"\nSo phan tu: {count}")
    while not aux.isEmpty():
        stack.push(aux.pop())
    print(f"Stack sau khoi phuc: {stack}")


s = Stack()
for val in [1, 2, 3]:
    s.push(val)

print(f"Stack ban dau: {s}\n")
display_and_count(s)
