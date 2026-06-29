class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if self.isEmpty():
            raise IndexError("Stack rong!")
        return self.data.pop()

    def isEmpty(self):
        return len(self.data) == 0


def reverse_string(s):
    stack = Stack()
    for ch in s:
        stack.push(ch)
    result = ""
    while not stack.isEmpty():
        result += stack.pop()
    return result


print(reverse_string("abc"))
print(reverse_string("hello"))
print(reverse_string("12345"))
