class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        
        cover = [0]*len(ranges)
        for i, v in enumerate( ranges ):
            l = max( 0, i-v )
            cover[l] = max( cover[l], i+v )
            
        ans = 0
        lo, hi = 0, 0
        while hi < n:
            lo, hi = hi, max( cover[ lo:hi+1 ] )
            if lo == hi: return -1
            ans += 1
        
        return ans
