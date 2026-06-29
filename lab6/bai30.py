from collections import deque

def round_robin(processes, quantum):
    queue = deque([(name, burst) for name, burst in processes])
    time = 0
    finish = {}

    while queue:
        name, remaining = queue.popleft()
        run = min(quantum, remaining)
        time += run
        remaining -= run
        if remaining > 0:
            queue.append((name, remaining))
        else:
            finish[name] = time

    for name, t in finish.items():
        print(f"{name} hoan thanh luc t={t}")


round_robin([("P1", 4), ("P2", 3), ("P3", 2)], quantum=2)
