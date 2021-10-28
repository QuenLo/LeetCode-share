## Binary Search
class Solution:

    def __init__(self, w: List[int]):
        
        self.sub = []
        sub_total = 0
        for weight in w:
            sub_total += weight
            self.sub.append(sub_total)
        
        self.total = sub_total

    def pickIndex(self) -> int:
        
        pick = random.randrange(1,self.total+1)
        high, low = len(self.sub), 0
        while low < high:
            mid = low + (high-low)//2
            if pick > self.sub[mid]:
                low = mid + 1
            else:
                high = mid
        
        return low

class Solution:

    def __init__(self, w: List[int]):
        
        self.sub = []
        sub_total = 0
        for weight in w:
            sub_total += weight
            self.sub.append(sub_total)
        
        self.total = sub_total

    def pickIndex(self) -> int:
        
        pick = random.randrange(1,self.total+1)
        for i, w in enumerate(self.sub):
            if w >= pick:
                return i
        
        return 0
