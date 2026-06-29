from collections import deque

def simulate(commands):
    queue = deque()
    for cmd in commands:
        parts = cmd.strip().split()
        if parts[0] == "enqueue":
            val = int(parts[1])
            queue.append(val)
            print(f"enqueue {val} -> {list(queue)}")
        elif parts[0] == "dequeue":
            if queue:
                val = queue.popleft()
                print(f"dequeue -> {val} | con lai: {list(queue)}")
            else:
                print("Underflow!")
    print(f"Trang thai cuoi: {list(queue)}")


simulate(["enqueue 5", "enqueue 7", "dequeue"])
