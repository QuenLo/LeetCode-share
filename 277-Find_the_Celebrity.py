# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class SolutionII:
    
    @lru_cache(maxsize=None)
    def cachedKnows(self, a, b):
        return knows(a, b)
    
    def findCelebrity(self, n: int) -> int:
        
        candidate = 0
        for i in range(1, n):
            if self.cachedKnows(candidate, i):
                candidate = i
        
        temp = True
        for j in range(n):
            if candidate == j: continue
            if self.cachedKnows(candidate,j) or not self.cachedKnows(j,candidate):
                temp = False
                break
        if temp:
            return candidate
        
        return -1

# Time Complexity : O(n)
Space Complexity : O(1)
class Solution:
    def findCelebrity(self, n: int) -> int:
        
        candidate = 0
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i
        
        temp = True
        for j in range(n):
            if candidate == j: continue
            if knows(candidate,j) or not knows(j,candidate):
                temp = False
                break
        if temp:
            return candidate
        
        return -1
