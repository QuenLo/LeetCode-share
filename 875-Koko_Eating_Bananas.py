class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        if len(piles) == h:
            return max( piles )
        
        
        s, l = 1, max(piles)
        
        while s < l:
            mid = (s+l) // 2
            total = sum( [(pile-1)//mid+1 for pile in piles] )
            
            if total > h:
                s = mid + 1
            else:
                l = mid
            
        return s
