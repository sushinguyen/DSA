from collections import deque

class HitCounter:
    def __init__(self, window=300):
        self.window = window
        self.queue  = deque()

    def hit(self, timestamp):
        self.queue.append(timestamp)

    def count(self, now):
        while self.queue and self.queue[0] <= now - self.window:
            self.queue.popleft()
        return len(self.queue)


hc = HitCounter(window=300)
hc.hit(1)
hc.hit(100)
hc.hit(200)
hc.hit(300)
print(hc.count(300))
hc.hit(400)
print(hc.count(400))
print(hc.count(600))
