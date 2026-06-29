class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop() if self.data else None

    def isEmpty(self):
        return len(self.data) == 0


def is_balanced(s):
    stack = Stack()
    match = {')': '(', ']': '[', '}': '{'}
    open_brackets  = set('([{')
    close_brackets = set(')]}')

    for ch in s:
        if ch in open_brackets:
            stack.push(ch)
        elif ch in close_brackets:
            if stack.pop() != match[ch]:
                return False

    return stack.isEmpty()


tests = ["([]{})","([)]","((())))","{[()]}","(]","","((("]
for t in tests:
    print(f"'{t}' -> {str(is_balanced(t)).lower()}")
