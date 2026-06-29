class AmortizedQueue:
    def __init__(self):
        self.in_stack  = []
        self.out_stack = []
        self.total_ops = 0

    def enqueue(self, value):
        self.in_stack.append(value)
        self.total_ops += 1

    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
                self.total_ops += 1
        if not self.out_stack:
            print("Underflow!")
            return None
        self.total_ops += 1
        return self.out_stack.pop()

    def report(self, n_ops):
        print(f"Tong thao tac thuc te: {self.total_ops}")
        print(f"So phep dequeue/enqueue: {n_ops}")
        print(f"Trung binh: {self.total_ops / n_ops:.2f} ops/thao tac")


q = AmortizedQueue()
n = 10
for i in range(1, n + 1):
    q.enqueue(i)
for _ in range(n):
    q.dequeue()

q.report(2 * n)
