from collections import deque

class HitCounter:

    def __init__(self):
        self.total = 0
        self.queue = deque()
        

    def hit(self, timestamp: int) -> None:
        
        if not self.queue or self.queue[-1][0] != timestamp:
            self.queue.append( [timestamp, 1] )
        else:
            self.queue[-1][1] += 1
        
        # print(self.queue, self.total)
        self.total += 1
        

    def getHits(self, timestamp: int) -> int:
        
        while self.queue and self.queue[0][0] <= timestamp - 300:
            self.total -= self.queue.popleft()[1]
        
        return self.total


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
