from collections import deque


class RecentCounter:

    def __init__(self):
        # number of recent call within [t-3000]
        self.queue = deque() # a queue for stream
        

    def ping(self, t: int) -> int:
        while len(self.queue) and self.queue[0] < t-3000:
            self.queue.popleft()
        self.queue.append(t)
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)